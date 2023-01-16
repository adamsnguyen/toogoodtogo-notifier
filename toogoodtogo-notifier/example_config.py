# Fill out the details and rename this file to config.py

tgtg = {
    "email": "xxx",
    "access_token": 'xxx',
    "refresh_token": 'xxx',
    "user_id": "xxx",
}

telegram = {
    "api_id": 123,
    "api_hash": "xxx",
    "bot_id": "xxx",
    "channel_id": 	-123,
    "bot_token": "xxx"
}

pia = {
    "user": "xxx",
    "pass": "xxx"
}

vpn = {
    "vpn-script-location": "/path/to/manual-connections",
    "vpn-script": "start-vpn.sh",
    "vpn-script-input": f"sudo VPN_PROTOCOL=wireguard DISABLE_IPV6=no DIP_TOKEN=no AUTOCONNECT=true PIA_PF=true PIA_DNS=true PIA_USER={pia['user']} PIA_PASS={pia['pass']}"
}