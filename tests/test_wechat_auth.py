import pytest

from src.auth.wechat import WeChatAuthService


def test_wechat_auth_service():
    service = WeChatAuthService(appid="wx_demo_appid", secret="demo_secret")
    res = service.exchange_code("mock_code_123")
    assert res["openid"] == "mock_openid_mock_code_123"

    with pytest.raises(ValueError, match="js_code 不能为空"):
        service.exchange_code("")
