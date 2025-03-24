import pygame
import sys

# Pygame кітапханасын инициализациялау
pygame.init()

# Терезе өлшемдері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Сурет салу")  # Терезенің атауын орнату

# Түстер
WHITE = (255, 255, 255)  # Ақ түс
BLACK = (0, 0, 0)  # Қара түс
RED = (255, 0, 0)  # Қызыл түс
BLUE = (0, 0, 255)  # Көк түс
GREEN = (0, 255, 0)  # Жасыл түс

# Айнымалылар
clock = pygame.time.Clock()  # Кадр жиілігін басқару үшін сағат
running = True  # Бағдарламаның жұмыс істеу күйі

drawing = False  # Сурет салу процесінің күйі
last_pos = None  # Алдыңғы позиция (сызықтар салу үшін)
color = BLACK  # Әдепкі түс - қара
radius = 5  # Қаламның қалыңдығы
mode = "pen"  # Сурет салу режимі (pen, eraser, rect, circle, line, triangle)
start_pos = None  # Бастапқы нүкте (суреттер салу үшін)

# Бастапқы бетті ақ түспен бояу
screen.fill(WHITE)

while running:
    for event in pygame.event.get():  # Барлық оқиғаларды тексеру
        if event.type == pygame.QUIT:  # Егер терезені жабу оқиғасы болса
            running = False  # Бағдарламаны тоқтату
        
        elif event.type == pygame.KEYDOWN:  # Пернелерді басу оқиғасы
            if event.key == pygame.K_c:
                screen.fill(WHITE)  # Экранды тазалау
            elif event.key == pygame.K_r:
                mode = "rect"  # Тіктөртбұрыш салу режимі
            elif event.key == pygame.K_o:
                mode = "circle"  # Шеңбер салу режимі
            elif event.key == pygame.K_l:
                mode = "line"  # Сызық салу режимі
            elif event.key == pygame.K_p:
                mode = "pen"  # Қалам режимі
            elif event.key == pygame.K_e:
                mode = "eraser"  # Өшіргіш режимі
            elif event.key == pygame.K_t:
                mode = "triangle"  # Үшбұрыш салу режимі
            elif event.key == pygame.K_1:
                color = BLACK  # Қара түсті таңдау
            elif event.key == pygame.K_2:
                color = RED  # Қызыл түсті таңдау
            elif event.key == pygame.K_3:
                color = BLUE  # Көк түсті таңдау
            elif event.key == pygame.K_4:
                color = GREEN  # Жасыл түсті таңдау

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Тышқанды басу оқиғасы
            drawing = True  # Сурет салу басталды
            start_pos = event.pos  # Бастапқы нүктені сақтау
            last_pos = event.pos  # Алдыңғы позицияны сақтау
            
        elif event.type == pygame.MOUSEBUTTONUP:  # Тышқанды жіберу оқиғасы
            drawing = False  # Сурет салу аяқталды
            if mode == "rect":  # Егер режим тіктөртбұрыш болса
                pygame.draw.rect(screen, color, pygame.Rect(start_pos, (event.pos[0] - start_pos[0], event.pos[1] - start_pos[1])), 2)
            elif mode == "circle":  # Егер режим шеңбер болса
                radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)
            elif mode == "line":  # Егер режим сызық болса
                pygame.draw.line(screen, color, start_pos, event.pos, 2)
            elif mode == "triangle":  # Егер режим үшбұрыш болса
                pygame.draw.polygon(screen, color, [start_pos, (event.pos[0], start_pos[1]), ((start_pos[0] + event.pos[0]) // 2, event.pos[1])], 2)

        elif event.type == pygame.MOUSEMOTION and drawing:  # Егер тышқан қозғалыста және сурет салу процесі жүріп жатса
            if mode == "pen":  # Егер режим қалам болса
                pygame.draw.line(screen, color, last_pos, event.pos, radius)  # Тышқан қозғалған сайын сызықтар салу
                last_pos = event.pos  # Алдыңғы позицияны жаңарту
            elif mode == "eraser":  # Егер режим өшіргіш болса
                pygame.draw.line(screen, WHITE, last_pos, event.pos, radius * 2)  # Ақ түспен өшіру
                last_pos = event.pos  # Алдыңғы позицияны жаңарту

    pygame.display.update()  # Экранды жаңарту
    clock.tick(60)  # Ойын кадр жиілігін шектеу (60 FPS)

pygame.quit()  # Pygame-ді жабу
sys.exit()  # Бағдарламаны жабу