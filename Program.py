import pygame
from random import randrange

RES = 800  # размер окна
SIZE = 50  # шаг

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)  # начальные координаты змейки
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)  # начальные координаты яблока
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1  # начальная длинна змейки
snake = [(x, y)]  # координаты всех точек змейки
dx, dy = 0, 0  # направление движения змейки
score = 0
fps = 5  # скорость змейки

pygame.init()  # инициализация модуля
sc = pygame.display.set_mode([RES, RES])  # создание рабочего окна
clock = pygame.time.Clock()  # объект для регулирования скорости змейки
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('1.jpg').convert()

while True:  # главный цикл
    sc.blit(img, (0, 0))
    # sc.fill(pygame.Color('black'))  # закрашиваем окно в черный цвет
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]  # рисуем зейку
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))  # рисуем яблоко

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    x += dx * SIZE  # определяем движение змейки
    y += dy * SIZE
    snake.append((x, y))  # добавляем точку в список коодинат
    snake = snake[-length:]  # убираем хвост змейки
    # реализация поедания яблока
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)  # начальные координаты яблока
        length += 1
        score += 1
        fps += 1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('red'))
            sc.blit(render_end, (RES // 2 - 175, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():  # контроль завершение программы
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()  # обновляем экран
    clock.tick(fps)  # делаем задержку

    for event in pygame.event.get():  # контроль завершение программы
        if event.type == pygame.QUIT:
            exit()

    # обозначаем клавиши движения
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
