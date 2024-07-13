import pygame

# init
pygame.init()
# variable running game
isRun = True

# membuat display surface object
app = pygame.display.set_mode((500,500))

# object game
# posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 1.5

while isRun: 
    pygame.time.delay(10)
    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
   
    if keys[pygame.K_RIGHT] and x < 500 - lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < 500 - panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # game dynamic

    # update asset
    app.fill((255,255,255))
    pygame.draw.rect(app, (255,0,0),(x,y,lebar,panjang))
    # render ke display
    pygame.display.update()


pygame.quit()