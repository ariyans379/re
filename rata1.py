# -*- coding: utf-8 -*-
# Edited from script LineVodka script made by Merkremont
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + "Thanks for add")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + "WELCOME to " + group.name)
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param3).displayName + " Good Bye\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + " Good Bye\n(*´･ω･*)")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                #if "gname:" in msg.text:
#--------------------------------------------------------------
                if msg.text == "Mulai":
                    print "ok"
                    _name = msg.text.replace("Mulai","")
                    gs = client.getGroup(msg.to)
                    sendMessage(msg.to,"▄︻̷̿┻̿═━一 FIRE! FIRE! FIRE!
o==[]::::::::::::::::> TUSUK MBLO!!!
──────────██
─────────█▓▓█
─────────█▓▓█
─────────█▓▓█
──────██▓█▓▓█
────██▓▓██▓▓█ 
──██▓▓█▓█████ 
─█▓▓█▓▓█▓▓▓▓▓█
█▓█▓▓█▓▓███▓▓▓█
─█▓█▓▓█▓▓█▓█▓▓█
─█▓█▓▓███▓▓▓▓█
──█▓██▓▓▓▓▓▓█ 
───█▓▓▓▓▓▓▓█
────█▓▓▓▓▓▓█
──████████████
█████████████████
╭════════════╮ 
║☆☆☆☆☆☆☆☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬██◥◤██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬◥◤╬╬◥◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬█◤╬╬☆║ 
║☆╬╬█████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬█████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬◢◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬╬◢██◣╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬██████╬╬☆║ 
║☆╬╬◤╬██╬◥╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬██╬╬╬╬☆║ 
║☆╬╬╬╬◥◤╬╬╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢◣╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬██◣╬╬╬╬╬☆║ 
║☆╬╬◥████◣╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██◤◥██╬╬☆║ 
║☆╬╬██╬╬██╬╬☆║ 
║☆╬╬██◣◢██╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆╬╬◢████◣╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬█████╬╬╬☆║ 
║☆╬╬██╬╬╬╬╬╬☆║ 
║☆╬╬◥████◤╬╬☆║ 
║☆╬╬╬╬╬╬╬╬╬╬☆║ 
║☆☆☆☆☆☆☆☆║ 
╰════════════╯
█████████████████
──████████████
────█▓▓▓▓▓▓█
────█▓▓▓▓▓▓▓█
───█▓██▓▓▓▓▓▓█ 
──█▓█▓▓███▓▓▓▓█
──█▓█▓▓█▓▓█▓█▓▓█ 
─█▓█▓▓█▓▓███▓▓▓█ 
──█▓▓█▓▓█▓▓▓▓▓█
───██▓▓█▓█████
─────██▓▓██▓▓█
───────██▓█▓▓█
──────────█▓▓█
──────────█▓▓█ 
──────────█▓▓█
───────────██
/¯ )
/¯ / 
/ /
/´¯/' '/´¯¯`•¸
/'/ / / /¨¯\
('( ( ( ( ¯~/' ')
\ ' /
\ _.•´
\ \
:v:v  :v  :v
:v  :v  :v  :v
:v  :v  :v  :v
:v:v  :v  :v
:v  :v
:v:v  :v  :v
:v  :v  :v  :v
:v  :v  :v  :v
:v:v  :v :v
:v
……..…../´¯/)……….. (\¯`\
…………/….//……….. …\\….\
………../….//………… ….\\….\
…../´¯/…./´¯\………../¯ `\….\¯`\
.././…/…./…./.|_……_| .\….\….\…\.\..
(.(….(….(…./.)..)..(..(. \….)….)….).)
.\…………….\/…/….\. ..\/……………./
..\…………….. /……..\……………..…/
….\…………..(………. ..)……………./
╔══╦═╦═╦══╦═╦═╦╦╦╗
║║║║║║║╠╗╔╣║║║║║║║
║║║║╦║║║║║║╦║╔╬╬╬╣
╚╩╩╩╩╩╩╝╚╝╚╩╩╝╚╩╩╝
SEKALEEEEE..........!!!!!!!!!!! 
DJIWAAAAA...........!!!!!!!!!!!
:V:V:V:V:V:V:V:V:V:V:V:V:V
BUKAN SULAP, BUKAN SIHIR
BUKAN KICKER, BUKAN HACKER
JARI GW GA SENGAJA KEPELINTIR
┌∩┐(◣_◢)┌∩┐ KZL???
━━━━━┒ MAMPOS LO!
┓┏┓┏┓┃
┛┗┛┗┛┃＼(-_-)／
┓┏┓┏┓┃ /
┛┗┛┗┛┃ ノ)
┓┏┓┏┓┃ 
┛┗┛┗┛┃ 
┓┏┓┏┓┃ 
┛┗┛┗┛┃ 
┓┏┓┏┓┃
┃┃┃┃┃┃
┻┻┻┻┻┻
SORRY YA MBLO. BUKAN GW YANG SALAH. SALAHIN JARI² GW YANG LAGI GABUT :v
☁☁🌞  ☁  ☁
☁  ✈  ☁  🚁  ☁  ☁  ☁  ☁  ☁ 
🏬🏨🏫🏢🏤🏥🏦🏪🏫
🌲/ l🚍\🌳👭
🌳/  🚘 l  🏃 \🌴 👬  👬  🌴/ l  🚔 \🌲
🌲/  🚖 l \
🌳/🚶 |  🚍 \ 🌴🚴🚴
🌴/ | \🌲
NAH KAN KALO KAYAK GINI UDAH ADEM NIH :v
Jurus kacqng Jurus Naga Kacang !!!
_█──░░─────███◣
_██─░░────████◣
_███░░───██⊙█◣
_.███░░──█████◣
_..███░░─█████◣
_..███░██████◣
_◢███████████◣
_◢███████████◣
◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
K____◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
A______◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
C________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
A_________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
N________◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
G______◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
_______◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
_________◥▓█倫KACANG倫 █▓◤
__________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
_________◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
_______◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
_______◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
_________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
_________◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
_______◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
K____◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
A______◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
C________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
A_________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG倫█▓◤
N________◥▓█倫KACANG倫█▓◤
________◥▓█倫KACANG倫█▓◤
G______◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
_____◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
__◥▓█倫KACANG倫█▓◤
___◥▓█倫KACANG倫█▓◤
____◥▓█倫KACANG倫█▓◤
K____◥▓█倫KACANG倫█▓◤
______◥▓█倫KACANG倫█▓◤
A______◥▓█倫KACANG倫█▓◤
________◥▓█k倫KACANG倫█▓◤
C________◥▓█倫KACANG倫█▓◤
__________◥▓█倫KACANG
RIP YOUR GRUP, JANGAN MACEM² YA MBLOO, ULAH LU KAYAK ALAY!!!
😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎
>>>>>>>>>> G O O D B Y E
😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂

GROUP LO KEDATANGAN TAMU BEGOOO!!!
TANGKISSS ANJING TANGKISSSS SEBELUM RUANG KOSONG!!!!!
¸.¤*¨¨*¤.¸¸...¸..¤\ 
\ ¸.¤*'``*¤.,,..,...¤ \
\ ¸ LEMAH \
\¸.¤*¨¨*¤.¸¸.¸..¤* \
\ 
O/ \ ~LEMAH~
/▌ \
/ \
████.RATA GAK RATA YG 
╬╬. PENTING PERNAH 
╬╬ ADA 
╬╬. . 
╬╬ 
╬╬\O 
╬╬ ▌\~ RATA YA 
╬╬// KAMI SENANG~
╬╬ 
╬╬ 
╬╬ 
╬╬
╬╬
╬╬\O ~GAK RATA
╬╬/▌LU BERUNTUNG~
╬╬/.\ 
█████ KIBARKAN BENDERA KEMATIAN
FUCK YOU GRUP
……..…../´¯/)……….. (\¯`\
…………/….//……….. …\\….\
………../….//………… ….\\….\
…../´¯/…./´¯\………../¯ `\….\¯`\
.././…/…./…./.|_……_| .\….\….\…\.\..
(.(….(….(…./.)..)..(..(. \….)….)….).)
.\…………….\/…/….\. ..\/……………./
..\…………….. /……..\……………..…/
….\…………..(………. ..)……………./
RATA GK RATA BODO AMAT YG PENTING PERNAH MAMPIR DIGIDAW
RATA KAMI SENANG
GK RATA KAMI JUGA SENANG
YG PENTING KAMI PERNAH MAMPIR DIGIDAW
SATPAM NYA LEMAH!!
MEMBERNYA PADA CUPU!!
DUA TIGA TUTUP BOTOL
TANGKIS KAMI KALO BISA TONGKOL
/¯ )
/¯ / 
/ /
/´¯/' '/´¯¯`•¸
/'/ / / /¨¯\
('( ( ( ( ¯~/' ')
\ LEMAH ' /
\ _.•´
\_ __ _ _/
~Fuck You~
⬛😈⬛⬛
░░ ███████ ]▄▄▄ ▄▄▃🔥
▂▄▅█████████▅▄▃ ▂
██████████████ █████
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤ ...
...
JANGAN DI LIATIN TANK KAMI!!!
TANGKIS JANGAN DIEM SAYANG!!!
SATPAM NYA LEMAH
MEMBERNYA PADA CUPU
IN ACTION
.._|\______________________,,
../ `--||||||||-------------------------]
./_==◎______________|-------/
...),----.(_(__) /
..//(¤) / ),----""
.//___///¯
/`---- ' |
|_____/
.........█▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤ .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤ .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤ .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤ .........█
▄▄▄▄▃
..▂▄▅█████▅▄▃▂
[███████████████
◥⊙▲⊙▲⊙▲⊙▲⊙◤ .........█
╔══╦═╦═╦══╦═╦═╦╦╦╗
║║║║║║║╠╗╔╣║║║║║║║
║║║║╦║║║║║║╦║╔╬╬╬╣
╚╩╩╩╩╩╩╝╚╝╚╩╩╝╚╩╩╝
Yah malah diliatin
TANGKIS GOBLOK
ini bagus kgk bro
JANGAN KANGEN YAH 😚😚😚
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▒▒▓▓▓▓▓▓
▓▓▓▒▒▓▒▒▓▓▓▓▓
▓▓▓▒▒▓▓▒▒▓▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▓▓▓▒▒▓▓▓
▓▓▓▒▒▒▒▒▒▒▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
Mati kamuh!!
( -_-)
<,︻╦╤─ ҉ - - - - - - -
/﹋\"
Mati kamuh!!
Mati kamuh!!
#SaveKicker :v
╬═╬ jangan turun kebawah
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬Halo?!..aku bilang jangan!
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
╬═╬
UDAH RATA, GA USAH LIAT :v")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendText(msg.to,"error")
#-------------------------------------------------------------			
		if msg.text == "speed":
                    start = time.time()
                    sendMessage(msg.to, "kecepatan koneksi")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------
                if msg.text == "nyanyi":
                    sendMessage(msg.to,"3")
                    sendMessage(msg.to,"2")
                    sendMessage(msg.to,"1")
                    sendMessage(msg.to,"Judul lagu JKT48 - oogoe diamond")
                    sendMessage(msg.to,"Ku mengejar bus yang mulai berjalan")
                    sendMessage(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    sendMessage(msg.to,"Kabut dalam hatiku telah menghilang")
                    sendMessage(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    sendMessage(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    sendMessage(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    sendMessage(msg.to,"Untukku menjadi diri sendiri")
                    sendMessage(msg.to,"Ku harus jujur, pada perasaanku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untukku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Saat ku sadari sesuatu menghilang")
                    sendMessage(msg.to,"Hati ini pun resah tidak tertahankan")
                    sendMessage(msg.to,"Sekarang juga yang bisa ku lakukan")
                    sendMessage(msg.to,"Merubah perasaan ke dalam kata kata")
                    sendMessage(msg.to,"Mengapa sedari tadi")
                    sendMessage(msg.to,"Aku hanya menatap langit")
                    sendMessage(msg.to,"Mataku berkaca kaca")
                    sendMessage(msg.to,"Berlinang tak bisa berhenti")
                    sendMessage(msg.to,"Di tempat kita tinggal, didunia ini")
                    sendMessage(msg.to,"Dipenuhi cinta, kepada seseorang")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Janji tak lepas dirimu lagi")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Akhirnya kita bisa bertemu")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Ku akan bahagiakan dirimu")
                    sendMessage(msg.to,"Ku ingin kau mendengarkan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Jika jika kamu ragu")
                    sendMessage(msg.to,"Takkan bisa memulai apapun")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga")
                    sendMessage(msg.to,"Jika kau bersuar")
                    sendMessage(msg.to,"Cahaya kan bersinar")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Sampaikan rasa sayangku ini")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriakkan ditengah angin")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untuk ku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Katakan dengan berani")
                    sendMessage(msg.to,"Jika kau diam kan tetap sama")
                    sendMessage(msg.to,"Janganlah kau merasa malu")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga..")
                    sendMessage(msg.to,"SPAM IS DONE")
                    sendMessage(msg.to,"Created By : Deka")
                    sendMessage(msg.to,"My: Kevin")
#-------------------------------------------------------------
                if msg.text == "Tagall":
		      group = client.getGroup(msg.to)
		      mem = [contact.mid for contact in group.members]
		      for mm in mem:
		       xname = client.getContact(mm).displayName
		       xlen = str(len(xname)+1)
		       msg.contentType = 0
                       msg.text = "@"+xname+" "
		       msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		       try:
                         client.sendMessage(msg)
		       except Exception as error:
                   	 print error
#-------------------------------------------------------------
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()
