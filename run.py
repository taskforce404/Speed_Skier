import pygame
import sys
sys.path.append("resources/")
from pygame.locals import *
from config import Config
from tools import creat_font
from Beibei import Beibei
from Countdown import Countdown
from Power import Power
from Obstacle import Obstacle
import random
from Food import Food
from Distance import Distance

#初始化pygame
pygame.init()
#创建clock对象，以控制帧率和获取帧时间
clock = pygame.time.Clock()
#创建屏幕对象
screen = pygame.display.set_mode((Config.SCREEN_WIDTH,Config.SCREEN_HEIGHT))
#最终滑行距离，初始值0
final_distance = 0

def start_sence():
    #创建start_sence界面，和screen尺寸相同
    start_sence = pygame.Surface((screen.get_rect().width,screen.get_rect().height))
    #主标题及位置
    welcome_text= creat_font("chinese",35).render("滑雪大作战",True,(150,150,150))
    welcome_text_rect = welcome_text.get_rect()
    welcome_text_rect.centerx = start_sence.get_rect().centerx
    welcome_text_rect.centery = start_sence.get_rect().centery-30
    #“开始”及位置
    #每1000毫秒发送事件，更改“开始”的显示状态，isShow为True时渲染，为False时不渲染
    start_text = creat_font("chinese",15).render("按START开始",True,(150,150,150))
    start_text_rect = start_text.get_rect()
    start_text_rect.centerx = start_sence.get_rect().centerx
    start_text_rect.centery = start_sence.get_rect().centery+50
    isShow = True
    e_change_show = USEREVENT+1
    pygame.time.set_timer(e_change_show,1000)
    #beibei图片，初始位置在屏幕右侧外边
    beibei_img = pygame.image.load('assets/images/skiing.png')
    beibei_img_rect = beibei_img.get_rect()
    beibei_img_rect.bottomleft = start_sence.get_rect().bottomright
    beibei_img_rect.x = beibei_img_rect.x + 50
    #dog图片，初始位置在屏幕左侧外边
    dog_img = pygame.image.load("assets/images/dog.png")
    dog_img_rect = dog_img.get_rect()
    dog_img_rect.bottomright = start_sence.get_rect().bottomleft
    dog_img_rect.x = dog_img_rect.x - 50

    while True:
        #设置帧率
        clock.tick(Config.FPS)
        #事件监听
        for e in pygame.event.get():
            #监听退出
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            #监听s键按下，按下之后开始运行main_sence方法（进入游戏界面）
            if e.type == KEYDOWN:
                if e.key == K_s:
                    main_sence()
                    break
            #监听e_change_show事件，如果此时isShow为True，设置为False；如果为False，则设置为True
            if e.type == e_change_show:
                if isShow:
                    isShow = False
                else:
                    isShow = True
        #start_sence填充背景色
        start_sence.fill(Config.BACKGROUND_COLOR)
        #start_sence渲染beibei图片
        start_sence.blit(beibei_img,beibei_img_rect)
        #（每一帧）判断beibei图片的位置，并设置x轴方向平移
        if beibei_img_rect.x > 256:
            beibei_img_rect.x = beibei_img_rect.x - 1
        #beibei图片位移到指定位置后，渲染主标题
        if beibei_img_rect.x <= 256:
            start_sence.blit(welcome_text,welcome_text_rect)
            #如果此时isShow为True，渲染开始
            if isShow:
                start_sence.blit(start_text,start_text_rect)
        #（每一帧）判断dog图片的位置，并设置x轴方向的平移
        start_sence.blit(dog_img,dog_img_rect)
        if dog_img_rect.x < 0:
            dog_img_rect.x = dog_img_rect.x + 1
        #将start_sence渲染在屏幕上
        screen.blit(start_sence,start_sence.get_rect())
        #显示更新
        pygame.display.update()

def main_sence():
    #声明全局变量final_distance
    global final_distance
    #main_sence
    main_sence = pygame.Surface((screen.get_rect().width,screen.get_rect().height))
    #创建beibei实例
    beibei = Beibei(main_sence)
    #创建倒计时实例
    countdown = Countdown(main_sence)
    #创建倒计时事件，每隔1000毫秒发送一次
    e_count_down = USEREVENT+1
    pygame.time.set_timer(e_count_down,1000)
    #创建一个障碍物group，该group中的sprite会被检测碰撞
    obstacle_group = pygame.sprite.Group()
    #运行开关，在倒计时结束时会被设置为True
    running = False
    #创建体力实例
    power = Power(main_sence)
    #创建默认体力扣减事件，每隔3000毫秒发送一次
    e_reduce_power = USEREVENT+2
    pygame.time.set_timer(e_reduce_power,3000)
    #创建障碍物的事件，每隔800毫秒发送
    e_creat_obstacle = USEREVENT+3
    pygame.time.set_timer(e_creat_obstacle,800)
    #创建食物事件，每隔5000毫秒发送
    e_creat_food = USEREVENT+4
    pygame.time.set_timer(e_creat_food,5000)
    #实例化距离类
    distance = Distance(main_sence)
    #每500毫秒发送一次增加距离事件
    e_add_distance = USEREVENT+5
    pygame.time.set_timer(e_add_distance,500)
    #创建碰撞对象列表
    collide_list = []

    while True:
        print(beibei.movespeed)
        #设置帧率
        clock.tick(Config.FPS)
        #事件监听
        for e in pygame.event.get():
            #监听退出
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            #监听倒计时事件
            if e.type == e_count_down:
                countdown.update_now()
                #当countdown.now为4时，设置running为True，游戏开始
                if countdown.now == 3:
                    running = True
            #监听默认体力扣减事件，每次扣减5体力
            if e.type == e_reduce_power:
                if running:
                    power.reduce_power(5)
            #监听创建障碍物事件，如果running为True，创建一个障碍物并添加到obstacle_group中
            if e.type == e_creat_obstacle:
                if running:
                    obstacle_group.add(Obstacle(main_sence,Config.OBSTACLES_LIST[random.randint(0,2)]))
            #监听创建食物事件，如果running为True，创建一个食物并添加到obstacle_group中
            if e.type == e_creat_food:
                if running:
                    obstacle_group.add(Food(main_sence))
            #监听增加距离事件，如果running为True，将调用distance实例的add_distance方法
            if e.type == e_add_distance:
                if running:
                    distance.add_distance()

            if e.type == KEYUP:
                beibei.movespeed = 2
                    
        #当游戏开始后，监听键盘按下，在屏幕范围内设置beibei实例前后左右移动
        if running:
            if pygame.key.get_pressed()[K_a]:
                if beibei.rect.x >= 0:
                    beibei.increase_movespeed(clock.get_time())
                    beibei.rect.x = beibei.rect.x - beibei.movespeed
            if pygame.key.get_pressed()[K_d]:
                if beibei.rect.x <= 320-64:
                    beibei.increase_movespeed(clock.get_time())
                    beibei.rect.x = beibei.rect.x + beibei.movespeed
            if pygame.key.get_pressed()[K_w]:
                if beibei.rect.y >= 0:
                    beibei.increase_movespeed(clock.get_time())
                    beibei.rect.y = beibei.rect.y - beibei.movespeed
            if pygame.key.get_pressed()[K_s]:
                if beibei.rect.y <= 240-64:
                    beibei.increase_movespeed(clock.get_time())
                    beibei.rect.y = beibei.rect.y + beibei.movespeed
        
        #与beibei实例碰撞的sprite会被添加到collide_list列表中，并将其在obstacle_group中删除
        collide_list = pygame.sprite.spritecollide(beibei,obstacle_group,True)
        #碰撞后逻辑
        for obj in collide_list:
            if obj.plus_power:
                power.power_num = power.power_num + obj.value
                if power.power_num > 80:
                    power.power_num = 80
            else:
                power.power_num = power.power_num - obj.value
                if power.power_num <= 0:
                    power.power_num = 0
        #判断power数值，如果为0，游戏结束，并将当前滑行距离赋值给全局变量final_distance
        if power.power_num <= 0:
            running = False       
            final_distance = distance.distance
            end_sence()
            break

        #main_sence填充背景色             
        main_sence.fill(Config.BACKGROUND_COLOR)
        #渲染beibei实例
        beibei.blitme(clock.get_time())
        #渲染倒计时实例
        countdown.blitme()
        #渲染距离实例
        distance.blitme()
        #obstacle_group执行update方法（该group里所有的sprite的update方法都会执行一遍）
        obstacle_group.update()
        #渲染体力实例
        power.blitme()
        #将main_sence渲染在屏幕上
        screen.blit(main_sence,main_sence.get_rect())
        #显示更新
        pygame.display.update()

def end_sence():
    #声明全局变量final_distance
    global final_distance
    #end_sence
    end_sence = pygame.Surface((screen.get_rect().width,screen.get_rect().height))

    message = "滑行距离 "+str(final_distance)+" 米"
    score_text = creat_font(size=35).render(message,True,(150,150,150))
    score_text_rect = score_text.get_rect()
    score_text_rect.centerx = end_sence.get_rect().centerx
    score_text_rect.centery = end_sence.get_rect().centery

    while True:
        clock.tick(Config.FPS)
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
            #按S重置final_distance为0，并运行main_sence，重新开始游戏
            if e.type == KEYDOWN:
                if e.key == K_s:
                    final_distance = 0
                    main_sence()
        
        end_sence.fill(Config.BACKGROUND_COLOR)
        end_sence.blit(score_text,score_text_rect)

        screen.blit(end_sence,end_sence.get_rect())

        pygame.display.update()

start_sence()





