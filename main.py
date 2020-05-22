#! /usr/bin/env python
# -*- coding: utf-8 -*-
print ("""
Working.
@muuT3ra$$uu-wall-b2
#FuckAllEverything. 
by Tripl_color vk.com/Tripl_color""")
import vk_requests
import time
id = str(input('Айди жертвы = '))
t = str(input('Кд постов = '))
att = 'photo384062261_457258115'
print ("by Tripl_color , started.")
msg = "Уебем всех инстасамок. By Tripl_color vk.com/tripl_color, @muuT3R@$$uu-wall-b2"
t1 = "token1"
t2 = "token2"
t3 = "token3"
t4 = "token4"
#t5 = ""

while True:
 api = vk_requests.create_api(service_token= t1)
 print(api.wall.post(owner_id= id, message= msg, attachments= 'photo587700708_457239806'))
 time.sleep(t)
 api = vk_requests.create_api(service_token= t2)
 print(api.wall.post(owner_id= id, message= msg, attachments= 'photo587700708_457239806'))
 time.sleep(t)
 api = vk_requests.create_api(service_token= t3)
 print(api.wall.post(owner_id= id, message= msg, attachments= 'photo587700708_457239806'))
 time.sleep(t)
 api = vk_requests.create_api(service_token= t4)
 print(api.wall.post(owner_id= id, message= msg, attachments= 'photo587700708_457239806'))
 time.sleep(t)
