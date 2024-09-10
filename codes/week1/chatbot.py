"""
Please set the environment variable `OPENAI_API_KEY` to your OpenAI API key,
and set the `OPENAI_BASE_URL` (optional) to the base URL for the OpenAI API.
"""

from openai import OpenAI


class ChatBot:
    def __init__(self):
        # 初始化上下文列表
        self.context = []
        self.client = OpenAI()

    def add_message(self, role, content):
        """将消息添加到上下文，并只保留最近的两次对话"""
        self.context.append({"role": role, "content": content})
        if len(self.context) > 4:
            self.context = self.context[-4:]

    def get_response(self, user_input):
        """获取机器人回复"""
        # 将用户输入添加到上下文
        self.add_message("user", user_input)

        # 调用 OpenAI API 获取回复
        response = self.client.chat.completions.create(
            model="gpt-4o", messages=self.context
        )

        # 提取并保存机器人的回复
        bot_reply = response.choices[0].message.content
        self.add_message("assistant", bot_reply)

        return bot_reply


if __name__ == "__main__":
    bot = ChatBot()
    print("欢迎使用SWUFE Bot！输入'quit'退出。")

    while True:
        user_input = input("你: ")
        if user_input.lower() == "quit":
            break
        res = bot.get_response(user_input)
        print("机器人：", res)
