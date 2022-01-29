from turtle import *
from time import sleep
from random import randint
# Подключи нужные модули

t1 = Turtle()
t1.point = 0
t1.color('red')
t1.penup()
t1.shape('turtle')
t1.speed(100)# Создай объект "черепашка", установи форму, цвет, скорость

x = 200
y = 200

def rand_move():
    t1.goto(randint(-x, x),randint(-y, y))
    
def catch(x,y):
    t1.write('A!', font=('Arial', 14, 'normal'))
    t1.point += 1
rand_move()#Определи функцию rand_move(), переносящую черепашку в случайную точку

t1.onclick(catch)# Определи функцию-обработчик catch(x, y), которая обработает клик по черепашке

while t1.point < 3:
    sleep(randint(1,2))
    rand_move()#Определи функцию rand_move(), переносящую черепашку в случайную точку
t1.write('WOW', font=('Arial', 14, 'normal'))
t1.hideturtle()
    # (успешные клики копятся в свойстве t.points)      

    # Создай подписку на событие «клик по объекту-черепашке»

    # Создай цикл, работающий пока кликов t.points меньше 3
