import random

def number_guessing_game():
    # 1에서 100까지의 랜덤한 숫자 생성
    secret_number = random.randint(1, 100)

    print("1에서 100 사이의 숫자를 맞춰보세요!")

    attempts = 0
    while True:
        user_guess = int(input("추측한 숫자를 입력하세요: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"축하합니다! {attempts}번 만에 숫자를 맞추셨습니다.")
            break
        elif user_guess < secret_number:
            print("너무 작아요. 다시 시도해보세요.")
        else:
            print("너무 크아요. 다시 시도해보세요.")

# 게임 실행
number_guessing_game()

