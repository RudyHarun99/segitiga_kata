'''
Soal 2 - 🔺 Segitiga Kata
Buatlah sebuah file python (.py) yang mengandung sebuah function dengan 1 parameter,
yang dapat membentuk pola segitiga dengan elemen berupa karakter-karakter
dari sebuah string yang menjadi parameter function tersebut.
Info selengkapnya silakan ikuti case flow beserta output yang diharapkan berikut ini.

Case Flow: Saat dieksekusi, program akan mencetak pola segitiga dari karakter-karakter string
yang diinputkan. Jika jumlah karakter string memenuhi syarat terbentuknya pola,
maka program akan menjalankannya. Namun jika jumlah karakter string tidak memenuhi
syarat membentuk pola, maka akan muncul pesan bahwa string tidak memenuhi syarat membentuk pola.

segitigaKata('Purwadhika')
segitigaKata('Purwadhika Startup and Coding School @BSD')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('lintang')
Output yang diharapkan:

# segitigaKata('Purwadhika')
P 
u r     
w a d   
h i k a 
p u r w 
a d h   
i k     
a   

# segitigaKata('Purwadhika Startup and Coding School @BSD')
P
u r
w a d 
h i k a
S t a r t
u p a n d C
o d i n g S c
h o o l @ B S D
P u r w a d h i
k a S t a r t
u p a n d C
o d i n g
S c h o
o l @
B S 
D

# segitigaKata('kode')
Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.

# segitigaKata('kode python')
k
o d
e p y
t h o n
k o d e
p y t
h o
n

# segitigaKata('lintang')
Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.
'''

# Jawaban

def segitigaKata(x):
    x=x.replace(' ','')
    panjang=len(x)
    valid=False
    counter=1
    while panjang!=0:
        if panjang-counter==0:
            valid=True
            x1=x
            i=0
            while len(x1)!=0:
                kata=''
                i+=1
                for j in range(i):
                    kata+=x1[j]+' '
                x1=x1[i:]
                print(kata)
            x2=x
            while len(x2)!=0:
                kata=''
                for k in range(i):
                    kata+=x2[k]+' '
                x2=x2[i:]
                print(kata)
                i-=1
            break
        elif panjang-counter>0:
            panjang-=counter
            counter+=1
        else:
            valid=False
            print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
            break

segitigaKata('Purwadhika')
segitigaKata('Purwadhika Startup and Coding School @BSD')
segitigaKata('kode')
segitigaKata('kode python')
segitigaKata('lintang')