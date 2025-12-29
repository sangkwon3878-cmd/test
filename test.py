import os
from dotenv import load_dotenv
from openai import OpenAI

# 수정

# 🔹 .env 파일 로드
load_dotenv()

# 🔹 OpenAI 클라이언트 생성
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 🔹 대화 히스토리 (system 메시지는 최초 1회만)
messages = [
    {
        "role": "system",
        "content": (
            "너는 친절하고 간결한 AI 어시스턴트다. "
            "욕설, 혐오 표현, 불법적인 내용은 절대 생성하지 말고 "
            "항상 한국어로만 대답해라."
        )
    }
]

print("🤖 GPT와 대화를 시작합니다. 종료하려면 'exit' 입력")

while True:
    user_input = input("🙋 사용자: ")

    if user_input.lower() == "exit":
        print("👋 대화를 종료합니다.")
        break

    # 🔹 사용자 메시지 추가
    messages.append({
        "role": "user",
        "content": user_input
    })

    # 🔹 GPT 호출
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=messages,
        max_output_tokens=300,
        temperature=0.3,
        top_p=0.9
    )

    # 🔹 GPT 응답 텍스트
    assistant_text = response.output_text

    print(f"🤖 GPT: {assistant_text}")

    # 🔹 GPT 응답도 대화 히스토리에 저장
    messages.append({
        "role": "assistant",
        "content": assistant_text
    })
