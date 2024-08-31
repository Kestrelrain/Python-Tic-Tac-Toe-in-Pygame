import pygame

counter = 0

xoro = False
# pygame setup
pygame.init()
pygame.font.init
my_font = pygame.font.SysFont('Comic Sans MS', 200)
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
running = True

rows, cols = (3, 3)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0]

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for rows in "1":
        print(arr)


    screen.fill("yellow")
    pygame.draw.line(screen,"black",(0,332),(500,332),5)
    pygame.draw.line(screen,"black",(0,166),(500,166),5)

    pygame.draw.line(screen,"black",(166,0),(166,500),5)
    pygame.draw.line(screen,"black",(332,0),(332,500),5)
    print(pygame.mouse.get_pos())

    if arr[0][0] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 20))
    if arr[0][0] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 20))

    if arr[0][1] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 20))
    if arr[0][1] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 20))

    if arr[0][2] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 20))
    if arr[0][2] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 20))


    if arr[1][0] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 186))
    if arr[1][0] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 186))

    if arr[1][1] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 186))
    if arr[1][1] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 186))

    if arr[1][2] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 186))
    if arr[1][2] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 186))


    if arr[2][0] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 336))
    if arr[2][0] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (34, 336))

    if arr[2][1] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 336))
    if arr[2][1] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (200, 336))

    if arr[2][2] == 1:
            X_at_02 = my_font.render('X', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 336))
    if arr[2][2] == 2:
            X_at_02 = my_font.render('O', False, (0, 0, 0))
            screen.blit(X_at_02, (360, 336))

    pygame.display.flip()


    x,y = pygame.mouse.get_pos()

    if x >= 0:
        if x <= 166:
            if y <= 166:
                pygame.event.get()
                if pygame.mouse.get_pressed()[0] and arr[0][0] == 0:

                    print("yay0-1")
                    counter += 1
                    if xoro == True:
                        arr[0][0] = 1
                    else:
                        arr[0][0] = 2

    if x >= 166:
        if x <= 332:
            if y <= 166:
                pygame.event.get()
                if pygame.mouse.get_pressed()[0] and arr[0][1] == 0:
                    
                    counter += 1
                    if xoro == True:
                        arr[0][1] = 1
                    else:
                        arr[0][1] = 2
                    print("yay0-2")
    print(counter)

    if x >= 332:
        if x <= 500:
            if y <= 166:
                pygame.event.get()
                if pygame.mouse.get_pressed()[0] and arr[0][2] == 0:
                    counter += 1
                    if xoro == True:
                        arr[0][2] = 1
                    else:
                        arr[0][2] = 2
                    print("yay0-3")

    if x >= 0:
        if x <= 166:
            if y >= 166:
                if y <= 332:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[1][0] == 0:
                        counter += 1
                        if xoro == True:
                            arr[1][0] = 1
                        else:
                            arr[1][0] = 2
                        print("yay1-1")
    if x >= 166:
        if x <= 332:
            if y >= 166:
                if y <= 332:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[1][1] == 0:
                        counter += 1
                        if xoro == True:
                            arr[1][1] = 1
                        else:
                            arr[1][1] = 2

                    print("yay1-2")
    if x >= 332:
        if x <= 500:
            if y >= 166:
                if y <= 332:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[1][2] == 0:
                        counter += 1
                        if xoro == True:
                            arr[1][2] = 1
                        else:
                            arr[1][2] = 2

                    print("yay1-3")


    if x >= 0:
        if x <= 166:
            if y >= 332:
                if y <= 500:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[2][0] == 0:
                        counter += 1
                        if xoro == True:
                            arr[2][0] = 1
                        else:
                            arr[2][0] = 2
                    print("yay2-1")
    if x >= 166:
        if x <= 332:
            if y >= 332:
                if y <= 500:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[2][1] == 0:
                        counter += 1
                        if xoro == True:
                            arr[2][1] = 1
                        else:
                            arr[2][1] = 2

                    print("yay2-2")
    if x >= 332:
        if x <= 500:
            if y >= 332:
                if y <= 500:
                    pygame.event.get()
                    if pygame.mouse.get_pressed()[0] and arr[2][2] == 0:
                        counter += 1
                        if xoro == True:
                            arr[2][2] = 1
                        else:
                            arr[2][2] = 2
                    print("yay2-3")

    if counter % 2 == 0:
        # even
        xoro = True
    else:
        # odd
        xoro = False
    print(xoro)
    


    clock.tick(24)

pygame.quit()