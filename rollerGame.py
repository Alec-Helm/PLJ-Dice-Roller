import pygame
from rollerFunctions import getRollData, add_text


#basic initializing stuff
pygame.init()
screen_size = (440,700)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('PLJ Dice Roller')
clock = pygame.time.Clock()




#create box to input number of dice, dice size, explosion set, reroll 1's toggle
num_dice_bar = pygame.Surface((150, 80))
num_dice_bar.fill('White')
num_dice_bar_rect = num_dice_bar.get_rect(topleft = [285, 10])
num_dice_typing = False


explosion_bar = pygame.Surface((150, 80))
explosion_bar.fill('White')
explosion_bar_rect = explosion_bar.get_rect(topleft = [285, 100])
explosion_typing = False

bonus_bar = pygame.Surface((150, 80))
bonus_bar.fill('White')
bonus_bar_rect = bonus_bar.get_rect(topleft = [285, 190])
bonus_typing = False

reroll_bar = pygame.Surface((40, 40))
reroll_bar.fill('Red')
reroll_bar_rect = reroll_bar.get_rect(topleft = [285, 280])


#create variables for inputs
num_dice = ''
explosion = ''
bonus = ''
reroll = False



#make the run button
run_bar = pygame.Surface((250, 60))
run_bar.fill('White')
run_bar_rect = run_bar.get_rect(topleft = [125, 340])



#style formatting
font = pygame.font.SysFont(None, 45)



while True:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()   
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if pygame.mouse.get_pressed()[0]:

                num_dice_typing = False
                explosion_typing = False
                bonus_typing = False

                position = pygame.mouse.get_pos()

                if num_dice_bar_rect.collidepoint(position):
                    num_dice_typing = True
 
                elif explosion_bar_rect.collidepoint(position):
                    explosion_typing = True

                elif bonus_bar_rect.collidepoint(position):
                    bonus_typing = True
                
                elif reroll_bar_rect.collidepoint(position):
                    reroll = not reroll
                    if reroll:
                        reroll_bar.fill('Green')
                    else:
                        reroll_bar.fill('Red')

                elif run_bar_rect.collidepoint(position):
                    explosions = [int(num) for num in explosion.split(",")]

                    getRollData(int(num_dice), explosions, int(bonus), 10000, int(bonus) + 50)


        elif event.type == pygame.KEYDOWN:
            #if we are in search mode, update the search box
            if num_dice_typing:
                if event.key == pygame.K_BACKSPACE:
                    num_dice = num_dice[:-1]
                else:
                    num_dice += event.unicode
            elif explosion_typing:
                if event.key == pygame.K_BACKSPACE:
                    explosion = explosion[:-1]
                else:
                    explosion += event.unicode
            elif bonus_typing:
                if event.key == pygame.K_BACKSPACE:
                    bonus = bonus[:-1]
                else:
                    bonus += event.unicode




    #cleanse screen
    screen.fill((0,0,0))


    #type static text
    add_text(screen, font, "Number of Dice", "White", [50, 10])
    add_text(screen, font, "Explosion Set", "White", [50, 100])
    add_text(screen, font, "Bonus", "White", [50, 190])
    add_text(screen, font, "Reroll 1's", "White", [50, 280])


    #draw the boxes for accepting input
    screen.blit(num_dice_bar, num_dice_bar_rect)
    screen.blit(explosion_bar, explosion_bar_rect)
    screen.blit(bonus_bar, bonus_bar_rect)
    screen.blit(reroll_bar, reroll_bar_rect)
    screen.blit(run_bar, run_bar_rect)


    #type current text into input boxes
    add_text(screen, font, num_dice, "Black", [290, 10])
    add_text(screen, font, explosion, "Black", [290, 100])
    add_text(screen, font, bonus, "Black", [290, 190])
    add_text(screen, font, "Run", "Black", [215, 360])

   
    



    

    




    #update the screen
    pygame.display.update()
    clock.tick(60)