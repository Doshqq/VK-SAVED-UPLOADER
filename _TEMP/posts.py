import requests


# SECRET_KEY = "vDXQB7wJfZqoBq6D8UAW"
TOKEN = "vk1.a.Ge78RcysUdoYHhCQOI_g5yAfqbgYq2gK1F8-dZFBhVSq91MCowPsAf25LKQIdaGFw1IKuXMNK0kRNA1F2KyYyk8H9RTdRNi1xln-1bN1AhSVnajhLXq_exkuViFtOQ7sMl7yoIqFJGnhum0hhwbJ9TbBDZVfIACsop25gZIa4RRBunzgadkrLF6lldA_nKcXpn_VaVUmwXi9Kj2vJAt0QA"
UPLOAD_URL = r"https://pu.vk.com/c855112/ss2186/upload.php?act=do_add&mid=289983025&aid=-3&gid=0&hash=179a452107192dc94f50ab98d20955e4&rhash=9f46179cacdf9214deaeb8e694079412&swfupload=1&api=1&mailphoto=1"

url = "https://api.vk.com/method/photos.getUploadServer"
params = {
    'access_token': TOKEN,
    'album_id': '-3',
    'v': '5.131'
}

files = {'photo': open('IMG_1270.jpg', 'rb')}

response = requests.post(UPLOAD_URL, files=files)
print(response.json())

# photo = '[{"markers_restarted":true,"photo":"6bb1bd7da8:w","sizes":[],"latitude":0,"longitude":0,"kid":"88d5d9ddbdab4748aa9aac0e52ae919b","sizes2":[["s","c195e8344a8aefe6aaba8dc7f9f146c0ff745b476e532662518ea7f2","-4763864001355950145",75,74],["m","153f576a8705d30826fd3ee563fbad14fcdaabf6f72790b1193f4509","-2358729147209323803",130,129],["x","f40aba0e1519816a367ce2fc152f4fc2e4f5df00839af66294050d44","6462826242458609331",604,600],["y","60153411a4b3758d3489cecf530148ae3919c9de086f71cbba4100a2","-3765601421369248768",807,802],["z","416e0df8743f44854d3c05c5429c1a9223ebe34f7648e066c8f4faf6","1017158049503605101",1087,1080],["w","20e9548be27ab5ec2d98e6c76b73886ae39f16c0c9c07ae462301ad4","-5575985778598706225",1170,1163],["o","153f576a8705d30826fd3ee563fbad14fcdaabf6f72790b1193f4509","-1855972596355944450",130,129],["p","a40ffa1217fadb5488c907c96c743c0984d1e4ecb8421cea604a4d02","3726394322998200663",200,199],["q","40c35a2a42601fd08be36093d0d52b06da76750e27898759d70c0df5","7254673980436771494",320,318],["r","1f22f781fcddfa70face76f7c01336256398b39d762eae5f40d38658","-6528467874785242311",510,507]],"urls":[],"urls2":["wZXoNEqK7-aquo3H-fFGwP90W0duUyZiUY6n8g/v1foSO5a470.jpg","FT9XaocF0wgm_T7lY_utFPzaq_b3J5CxGT9FCQ/5Wo6c1YcRN8.jpg","9Aq6DhUZgWo2fOL8FS9PwuT13wCDmvZilAUNRA/s2bR2jmSsFk.jpg","YBU0EaSzdY00ic7PUwFIrjkZyd4Ib3HLukEAog/AHSUUXXlvcs.jpg","QW4N-HQ_RIVNPAXFQpwakiPr4092SOBmyPT69g/bXEXXdurHQ4.jpg","IOlUi-J6tewtmObHa3OIauOfFsDJwHrkYjAa1A/z4P-KXoenrI.jpg","FT9XaocF0wgm_T7lY_utFPzaq_b3J5CxGT9FCQ/_i9YycFCPuY.jpg","pA_6Ehf621SIyQfJbHQ8CYTR5Oy4QhzqYEpNAg/VwlXu-TPtjM.jpg","QMNaKkJgH9CL42CT0NUrBtp2dQ4niYdZ1wwN9Q/pvIzXYzHrWQ.jpg","HyL3gfzd-nD6znb3wBM2JWOYs512Lq5fQNOGWA/OVPgow45ZqU.jpg"]}]'

# server = 855112
# hash_value = 'bde7a5a75b637d51b15bfae818b4bda1'
# # photo = '6bb1bd7da8:w'

# url = 'https://api.vk.com/method/photos.copy'
# params = {
#     'photo': photo,
#     # 'photos_list': photo,
#     'server': server,
#     'hash': hash_value,
#     'album_id': -3,
#     'access_token': TOKEN,
#     'v': '5.131'
# }
# print(params['photo'])

# response = requests.post(url, params=params)
# print(response.json())