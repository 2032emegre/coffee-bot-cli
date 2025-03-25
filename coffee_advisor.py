import os
import openai
from dotenv import load_dotenv

class CoffeeAdvisor:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("APIキーが設定されていません")
        
        openai.api_key = api_key

    def get_coffee_recommendation(self, mood: str) -> dict:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": """フレンドリーなバリスタとして、カジュアルな口調で回答してください。
以下の形式で具体的に答えてください：

コーヒー：[産地 + 焙煎度 + 特徴的な品種や製法など]
おすすめポイント：[その気分にぴったりな理由を1-2文で]
一言：[フランクなアドバイスや飲み方のコツ]"""},
                {"role": "user", "content": f"今の気分は「{mood}」なんだけど、おすすめのコーヒーを教えてほしいな"}
            ],
            max_tokens=180,
            temperature=0.8,  # より創造的な回答を得るために少し上げる
            presence_penalty=0.1  # 多様な表現を促す
        )

        return {
            "response": response.choices[0].message['content']
        } 