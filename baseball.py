import random

def generate_secret_number():
    # 0부터 9까지의 숫자 중에서 중복 없이 4개를 선택하여 비밀 숫자 생성
    return random.sample(range(10), 4)

def check_guess(secret, guess):
    # 숫자와 위치가 일치하는지, 숫자만 일치하는지 확인
    exact_matches = sum(a == b for a, b in zip(secret, guess))
    partial_matches = sum(a in secret for a in guess) - exact_matches
    return exact_matches, partial_matches

def baseball_game():
    print("숫자야구 게임을 시작합니다!")

    # 비밀 숫자 생성
    secret_number = generate_secret_number()

    attempts = 0
    while True:
        # 사용자에게 숫자 입력 받기
        user_input = input("4자리 숫자를 입력하세요: ")

        # 입력이 4자리인지 확인
        if len(user_input) != 4 or not user_input.isdigit():
            print("올바른 형식의 숫자를 입력하세요.")
            continue

        user_guess = [int(digit) for digit in user_input]

        # 입력한 숫자와 비교하여 결과 출력
        exact, partial = check_guess(secret_number, user_guess)
        attempts += 1

        print(f"결과: {exact}Strike, {partial}Ball")

        # 정답일 경우 게임 종료
        if exact == 4:
            print(f"축하합니다! {attempts}번 만에 숫자를 맞추셨습니다.")
            break

# 게임 실행
baseball_game()

