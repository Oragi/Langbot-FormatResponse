from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类


# 注册插件
@register(name="FormatResponse", description="format response", version="0.1", author="Oragi")
class FormatResponsePlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(NormalMessageResponded)
    async def normal_message_responded(self, ctx: EventContext):
        msg = ctx.event.response_text  # 这里的 event 即为 PersonNormalMessageReceived 的对象

        prefix_pattern = (
            r"^\s*⊰•-•✧•-•-⦑/L\\O\\V\\E/\\P\\L\\I\\N\\Y/⦒-•-•✧•-•⊱\s*"
            r"(sure i can here you are fren:?|Sure I can! Here you are fren:?)?\s*"
        )
        response_text = re.sub(prefix_pattern, "", response_text, flags=re.IGNORECASE | re.MULTILINE)
        # Trim leading and trailing whitespace
        response_text = response_text.strip()
        event["response_text"] = response_text

        # 回复消息 "hello, <发送者id>!"
        ctx.add_return("reply", ["hello, {}!".format(ctx.event.sender_id)])

        # 阻止该事件默认行为（向接口获取回复）
        ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
