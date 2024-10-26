# RCON คืออะไร
RCON หรือ Remote Console เป็นโปรโตคอลที่ใช้ TCP/IP ซึ่งอนุญาตให้ผู้ดูแลเซิร์ฟเวอร์สามารถรันคำสั่ง Minecraft จากระยะไกลได้ ถูกนำเสนอในเวอร์ชัน Beta 1.9-pre4 ซึ่งโดยพื้นฐานแล้วเป็นการนำโปรโตคอล Source RCON มาใช้กับ Minecraft
### _ข้อมูลต้นฉบับ: [RCON](https://wiki.vg/RCON)_
# คำสำคัญที่น่าสนใจในไฟล์ server.properties เพื่อใช้งาน RCON
|คำสำคัญ|ชนิดข้อมูล|ค่าโดยปริยาย| รายละเอียด|
|:-|:-|:-|:-|
|broadcast-rcon-to-ops|boolean|true|ให้คำสั่งของ RCON ส่งไปยังผู้เล่นยศ Operator ทั้งหมดที่กำลังออนไลน์อยู่|
|enable-rcon|boolean|false|ต้องการเปิดใช้งาน RCON หรือไม่ หากเปิดจะเป็นการอนุญาติให้เข้าถึง Console เซิร์ฟเวอร์ผ่าเครือข่าย ไม่แนะนำให้เชื่อมต่อกับ RCON ผ่านเครือข่ายที่ไม่น่าเชื่อถือ เช่น อินเทอร์เน็ต เนื่องจากข้อมูลไม่ถูกเข้ารหัส ข้อมูลทั้งหมดที่ส่งระหว่างไคลเอนต์และเซิร์ฟเวอร์ (รวมถึงรหัสผ่าน RCON) สามารถถูกดักจับได้ โดยทั่วไปแล้ว ควรเชื่อมต่อกับ RCON จาก localhost หรือ 127.0.0.1 เท่านั้น|
|rcon.password|string|blank|เป็นรหัสผ่านสำหรับ RCON หากรหัสผ่านว่างเปล่าแต่ RCON ถูกเปิดใช้งาน ระบบจะไม่เริ่มทำงานเพื่อเป็นการป้องกัน|
|rcon.port|integer (1-(2^16 - 2))|25575|หมายเลขพอร์ต TCP ที่ RCON เฝ้าฟังอยู่|
### _ข้อมูลต้นฉบับ: [Minecraft Wiki](https://minecraft.wiki/w/Server.properties)_
# ในตัวอย่างนี้ใช้โมดูล [mcrcon](https://pypi.org/project/mcrcon/) ในการใช้ RCON ด้วยภาษาไพทอน
# การกำหนดค่าในไฟล์ server.properties
```shell
broadcast-rcon-to-ops=true
enable-rcon=true
rcon.password=p@ssword # ควรตั้งรหัสผ่านเอง
rcon.port=25575 # สามารถเปลี่ยนได้ตามความเหมาะสม
```
# การกำหนดค่าในไฟล์ main.py
```python
from mcrcon import MCRcon, MCRconException

host = '127.0.0.1' # แนะนำให้เป็น localhost หรือ 127.0.0.1 เพื่อความปลอดภัย
password = 'p@ssword' # รหัสผ่านต้องตรงกันกับ rcon.password
port = 25575 # หมายเลขพอร์ตต้องตรงกันกับ rcon.port
tlsmode = 0
timeout = 5

try:
    with MCRcon(host, password, port, tlsmode, timeout) as mcr:
        resp = mcr.command('whitelist add NatchaLatte') # คำสั่งที่จะส่งไปยัง Minecraft server
        print(resp) # ส่งคำสั่งไปยัง Minecraft server
        resp = mcr.command('time set 0') # คำสั่งที่จะส่งไปยัง Minecraft server
        print(resp) # ส่งคำสั่งไปยัง Minecraft server
        resp = mcr.command('say LearnMinecraftRCONWithPython Succes!') # คำสั่งที่จะส่งไปยัง Minecraft server
        print(resp) # ส่งคำสั่งไปยัง Minecraft server
except MCRconException as e:
    print(e)
```

# ความแตกต่างของการกำหนดค่า broadcast-rcon-to-ops
```shell
broadcast-rcon-to-ops=true
```
![broadcast-rcon-to-ops=true](/assets/images/broadcast-rcon-to-ops=true.png "broadcast-rcon-to-ops=true")
```shell
broadcast-rcon-to-ops=false
```
![broadcast-rcon-to-ops=false](/assets/images/broadcast-rcon-to-ops=false.png "broadcast-rcon-to-ops=false")
