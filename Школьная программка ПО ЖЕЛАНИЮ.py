import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройки игры
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()


def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))


class Snake:
    def _init_(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + x) % GRID_WIDTH
        new_y = (head[1] + y) % GRID_HEIGHT
        new_position = (new_x, new_y)

        if new_position in self.positions[1:]:
            return False  # Игра окончена

        self.positions.insert(0, new_position)
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def grow(self):
        self.length += 1
        self.score += 1

    def change_direction(self, direction):
        # Запрещаем движение в противоположном направлении
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, GREEN, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)


class Food:
    def _init_(self, snake_positions):
        self.position = self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        while position in snake_positions:
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        return position

    def draw(self, surface):
        rect = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)


def show_game_over(score):
    font = pygame.font.SysFont('Arial', 36)
    text = font.render(f'Игра окончена! Счет: {score}', True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    restart_font = pygame.font.SysFont('Arial', 24)
    restart_text = restart_font.render('Нажмите R для перезапуска', True, WHITE)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.update()


def main():
    snake = Snake()
    food = Food(snake.positions)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        # Перезапуск игры
                        snake = Snake()
                        food = Food(snake.positions)
                        game_over = False
                else:
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))

        if not game_over:
            # Обновление игры
            if not snake.update():
                game_over = True

            # Проверка на съедание пищи
            if snake.get_head_position() == food.position:
                snake.grow()
                food = Food(snake.positions)

            # Отрисовка
            screen.fill(BLACK)
            draw_grid()
            snake.draw(screen)
            food.draw(screen)

            # Отображение счета
            font = pygame.font.SysFont('Arial', 24)
            score_text = font.render(f'Счет: {snake.score}', True, WHITE)
            screen.blit(score_text, (10, 10))

            pygame.display.update()
            clock.tick(FPS)
        else:
            show_game_over(snake.score)


if __name__ == "__main__":
    main()