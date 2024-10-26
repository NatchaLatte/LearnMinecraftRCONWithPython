from mcrcon import MCRcon, MCRconException

host = '127.0.0.1'
password = 'p@ssword'
port = 25575
tlsmode = 0
timeout = 5

try:
    with MCRcon(host, password, port, tlsmode, timeout) as mcr:
        resp = mcr.command('whitelist add NatchaLatte')
        print(resp)
        resp = mcr.command('time set 0')
        print(resp)
        resp = mcr.command('say LearnMinecraftRCONWithPython Succes!')
        print(resp)
except MCRconException as e:
    print(e)