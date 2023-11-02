from nonebot import get_driver
from pydantic import Field, BaseModel


class Config(BaseModel):
    saa_qqguild_use_magic_msg_id_to_send: bool = Field(
        False, description="是否使用魔法消息ID发送消息(msg_id='1000'), 用于绕过主动消息频率限制"
    )

    class Config:
        extra = "ignore"


global_config = get_driver().config
plugin_config = Config.parse_obj(global_config)
