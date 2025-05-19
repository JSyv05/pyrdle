import pygame, sys, random

pygame.init()

WIDTH, HEIGHT = 633, 900
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
                        else:
                            invalidFlag = True
                else:
                    if len(curr_word) < LETTER_LENGTH:
                        if event.unicode.isalpha():
                            curr_word += event.unicode.upper()
                            curr_letter += 1

        SCREEN.fill(BG)
        pygame.display.update()


if __name__ == "__main__":
    main()
