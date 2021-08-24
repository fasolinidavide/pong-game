import pygame

# pyagame module
pygame.init()

win = pygame.display.set_mode((750, 500))

pygame.display.set_caption('Pong')

white = (255, 255, 255)
black = (0, 0, 0)

# classi
class Paddle(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 100]) 
        self.image.fill(white) #colore 
        self.rect = self.image.get_rect() # rect: da la posizione dell'oggetto in quel momento
        self.point = 0 # punti
        self.speed = 10

class Pong(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(white)
        self.rect = self.image.get_rect() 
        self.speed = 10
        self.dx = 1
        self.dy = 1 

# posizionamento iniziale e variabile per definire le classi
paddle1 = Paddle()  
paddle1.rect.x = 25 
paddle1.rect.y = 225

paddle2 = Paddle()
paddle2.rect.x = 715
paddle2.rect.y = 225

pong = Pong()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, pong)


def redraw():
    win.fill(black)

    # titolo centrale
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render('Pong', False, white)
    textRect = text.get_rect()
    textRect.center = (750//2, 25)
    win.blit(text, textRect)

    # punteggio giocatore 1
    p1_score = font.render(str(paddle1.point), False, white)
    scoreP1Rect = p1_score.get_rect()
    scoreP1Rect.center = (50, 50)
    win.blit(p1_score, scoreP1Rect)

    # punteggio giocatore 2
    p2_score = font.render(str(paddle2.point), False, white)
    scoreP2Rect = p2_score.get_rect()
    scoreP2Rect.center = (700, 50)
    win.blit(p2_score, scoreP2Rect)

    all_sprites.draw(win) # ridisegnare tutti gli elementi sullo schermo 
    pygame.display.update()


def main():
    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        # movimento tramite tastiera
        key = pygame.key.get_pressed()
    
        if key[pygame.K_w]:
            paddle1.rect.y += -paddle1.speed
        if key[pygame.K_s]:
            paddle1.rect.y += paddle1.speed

        if key[pygame.K_UP]:
            paddle2.rect.y += -paddle2.speed 
        if key[pygame.K_DOWN]:
            paddle2.rect.y += paddle2.speed  

    
        # movimento della pallina 
        pong.rect.x +=  pong.speed * pong.dx
        pong.rect.y +=  pong.speed * pong.dy
    
        # collisione con i margini sopra e sotto
        if pong.rect.y > 490:
            pong.dy = -1

        if pong.rect.y < 10:
            pong.dy = 1 

        # collisione margini dx e sx
        if pong.rect.x > 740:
            pong.rect.x, pong.rect.y = 375, 250 # riposizionamento
            pong.dx = -1
            paddle1.point += 1
    
        if pong.rect.x < 10:
            pong.rect.x, pong.rect.y = 375, 250
            pong.dx = 1
            paddle2.point += 1

        # collisione con i racchette
        if paddle1.rect.colliderect(pong.rect):
            pong.dx = 1
        if paddle2.rect.colliderect(pong.rect):
            pong.dx = -1 
        
        redraw()

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        win.fill(black)
        title_label = title_font.render("Press the mouse to begin...", 1, (white))
        win.blit(title_label, (750/2 - title_label.get_width()/2, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()