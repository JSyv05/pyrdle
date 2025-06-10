import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pyrdle")
FPS = 30

GRAY = (124, 127, 147)
GREEN = (166, 209, 137)
YELLOW = (229, 200, 144)
BG = (165, 173, 206)
TEXT = (48, 52, 70)
WHITE_TEXT = (198, 208, 245)

LETTER_BOX_FONT_SIZE = 40

LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT = 60, 60

BOX_PADDING = 40
NUM_ROWS, NUM_COLUMNS = 6, 5

LETTER_LENGTH = NUM_COLUMNS

DX, DY = 10, 10
PADDING_X, PADDING_Y = 5, 5

BASE_OFFSET_X = (
    (WIDTH / 2)
    - ((NUM_COLUMNS / 2) * DX)
    - ((NUM_COLUMNS / 2) * LETTER_BOX_WIDTH)
    + (((NUM_COLUMNS + 1) % 2) * (DX / 2))
)
BASE_OFFSET_Y = (
    (HEIGHT / 2)
    - ((NUM_ROWS / 2) * DY)
    - ((NUM_ROWS / 2) * LETTER_BOX_HEIGHT)
    + (((NUM_ROWS + 1) % 2) * (DY / 2))
)

LETTER_BOX_FONT = pygame.font.Font("assets/CascadiaCode.ttf", LETTER_BOX_FONT_SIZE)


def main():
    answerList = open("assets/valid-wordle-answers.txt").read().splitlines()
    wordList = open("assets/valid-wordle-words.txt").read().splitlines()
    chosenWord = random.choice(answerList)
    currWord = ""
    currLetter = 0
    wordCount = 0
    rects = []
    usedWords = []
    invalidFlag = False
    tooShortFlag = False
    winFlag = False
    loseFlag = False
    guesses = 0
    assert len(chosenWord) == 5
    assert chosenWord.islower()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if currWord:
                        currWord = currWord[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(currWord) == LETTER_LENGTH:
                        if currWord.lower() in wordList:
                            wordCount += 1
                            usedWords.append(currWord)
                            currWord = ""
                            currLetter = 0
                            guesses += 1
                        else:
                            invalidFlag = True
                else:
                    if len(currWord) < LETTER_LENGTH:
                        if event.unicode.isalpha():
                            currWord += event.unicode.upper()
                            currLetter += 1
                print(currWord)

        SCREEN.fill(BG)

        for y in range(NUM_ROWS):
            row_rects = []
            for x in range(NUM_COLUMNS):
                x_pos = BASE_OFFSET_X + (x * DX) + (x * LETTER_BOX_WIDTH)
                y_pos = BASE_OFFSET_Y + (y * DY) + (y * LETTER_BOX_HEIGHT)
                curr_rect = pygame.Rect(
                    (x_pos, y_pos), (LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT)
                )
                pygame.draw.rect(SCREEN, WHITE_TEXT, curr_rect, 2)
                row_rects.append((x_pos, y_pos))
            rects.append(row_rects)
        pygame.display.update()


if __name__ == "__main__":
    main()
