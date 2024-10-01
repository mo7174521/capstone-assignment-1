from turtle import *

def draw_star(x, y, size, angle, color):
    """绘制并填充一个五角星"""
    penup()
    goto(x, y)
    setheading(angle)  # 调整星星的角度
    pendown()
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def draw_china_flag():
    # 设置画布和速度
    setup(800, 600)
    speed(10)
    bgcolor("red")

    # 绘制左上角的大星星
    draw_star(-350, 200, 100, 0, "yellow")

    # 绘制右边四颗小星星
    draw_star(-200, 270, 50, -30, "yellow")  # 第一颗小星星
    draw_star(-150, 200, 50, 0, "yellow")    # 第二颗小星星
    draw_star(-150, 120, 50, 30, "yellow")   # 第三颗小星星
    draw_star(-200, 70, 50, 60, "yellow")    # 第四颗小星星

    # 完成绘制
    penup()
    goto(0, 0)
    done()

draw_china_flag()
