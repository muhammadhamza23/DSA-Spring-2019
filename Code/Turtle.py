# This is the code for turtle GUI for lowerground and 2nd floor.
import turtle

Title=turtle.Screen()
Student=turtle.Turtle()
background=turtle.Screen()

Title.title('Lower Ground and 2nd Floor')
background.bgpic('Lower Ground.gif')
#background.bgpic('2nd Floor.gif')
Student.color('orange')
Student.width(10)
Student.speed(1)

#Student.setposition(-250,70)

Student.hideturtle()  
Student.penup()

Student.goto(-510, -22)
Student.showturtle()
Student.pendown()
Student.goto(-400, -22)
Student.goto(-400, -9)
Student.goto(-400, 12)
Student.goto(-400, 20)
Student.goto(-400, 45)
Student.goto(-400, 60)
Student.goto(-294, 60)
Student.goto(-280, 60)
Student.goto(-255, 60)
background.bgpic('2nd Floor.gif')
Student.clear()
Student.goto(-250, 70)
background.bgpic('2nd Floor.gif')
Student.goto(-250, 70)
background.bgpic('2nd Floor.gif')
Student.goto(-250, 70)
background.bgpic('2nd Floor.gif')
Student.goto(-250, 35)

Student.color('red')
