# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:42:48 2020

@author: kidominox
"""
def decision(json_box,light):
    
   
    red_light = 0
    green_light = 1
    yellow_light = 2
    orange_barrier = 3
    people = 4
    turn_left = 5
    go_straight = 6
    stop_card = 7
    side_walk = 8 #not used
    stop_line = 9
    
    """
    favor:通过对某一时刻的所有障碍物进行密度统计，小车更加倾向于往密度较小的方向进行偏转
    golbal const car_left_edge:小车在摄像头照片中的位置左边界
    golbal car_right_edge:小车在摄像头照片中的位置右边界
    priority:优先级
    light_Threshold:灯亮度的阙值
    light
    stop_distance:减速停止的阙值
    
    识别json数据格式：{"frame_id": 284, "bboxes": [{"x_min": 0, "y_min": 187, 
    "x_max": 124, "y_max": 291, "label": 1, "score": 55}]}
    """
    #之后补上初始值
    """
    stop_distance
    car_adopt_threshold
    orange_barrier_real_h
    orange_barrier_real_w
    people_real_h
    people_real_w
    light_Threshold = 40
    stop_distance = 3
    """
    if light<light_Threshold:
        #单片机控制
        light_control()
    traffic_sign = ''
    is_stop_line = False
    is_turn_left = False
    is_go_straight = False
    stop_line_y_max = 0
    traffic_line_status = ''
    for i in json_box:
        if i['label'] == stop_card:
            traffic_sign = 'stop'
        elif i['label'] == red_light and not traffic_sign == 'stop':
            traffic_sign = 'red'
        elif i['label'] == green_light and not traffic_sign == 'stop':
            traffic_sign ='green'
        elif i['label'] == yellow_light and not traffic_sign == 'stop':
            traffic_sign = 'yellow'
        elif i['label'] == 'stop_line':
            is_stop_line = True
            stop_line_y_max = i['y_max']
        elif i['label'] == 'turn_left':
            is_turn_left = True
        elif i['label'] == 'go_straight':
            is_go_straight = True
        #对于偏航的车，怎么辨别他在哪一个车道
        
    ##对于可能重复出现检测框采用循环的形式
    ##对于只出现一种情况或者没有出现采用变量的形式
    
    for i in json_box:
        if i['label']==people and priority == 1:
            if not (i['x_max' car_left_edge and i['x_min'] >= car_right_edge):
                distance = process_postion(x_min=i['x_min'],y_min=i['y_min'],
                                       x_max=i['x_max'],y_max=i['y_max'],
                                       width=people_real_w,height=people_real_h)
                if distance <= stop_distance:
                    stop_process()
                    priority = 0
                    #未完善
    for i in json_box:
        if i['label']==orange_barrier and priority == 1:
            if not (i['x_max' car_left_edge and i['x_min'] >= car_right_edge):
                distance = process_postion(x_min=i['x_min'],y_min=i['y_min'],
                                       x_max=i['x_max'],y_max=i['y_max'],
                                       width=orange_barrier_real_w,height=orange_barrier_real_h)
                if distance <= car_adopt_threshold and traffic_sign == 'green':
                    car_adopt()
                    priority = 0
                    #未完善
        if traffic_sign == "stop" and priority == 1:
            quick_stop_process()
            
        if (traffic_sign == 'red' or traffic_sign == 'yellow') and priority == 1:
            stop_process()
            #和行人一样
def qucik_process():
    #急刹车
        
def stop_process():
    #伪码：
    #如果有停止线is_stop_line == True 
    # 必须在前面停止！
    #如果没有可以减速停止
    停止线
    然后减速
def car_adopt():
    #避障
def light_control():
    
    #单片机控制
        
    
            
                        
        
                
    
