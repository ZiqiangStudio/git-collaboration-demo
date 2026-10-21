"""微信小程序登录授权服务（开发草稿态）。"""


class WeChatAuthService:
    """处理微信小程序 jscode2session 登录凭据置换。"""

    def __init__(self, appid: str, secret: str):
        self.appid = appid
        self.secret = secret

    def exchange_code(self, js_code: str) -> dict:
        # TODO: 接入实际腾讯微信 OpenAPI 请求网络调用
        if not js_code:
            raise ValueError("js_code 不能为空")
        return {
            "openid": f"mock_openid_{js_code}",
            "session_key": "mock_session_key",
        }
