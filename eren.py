# Terminalde "EREN" yazdıran Python kodu
print(" EEEE   RRRR   EEEE   N   N")
print(" E      R   R  E      NN  N")
print(" EEEE   RRRR   EEEE   N N N")
print(" E      R R    E      N  NN")
print(" EEEE   R  RR  EEEE   N   N")



import subprocess
import sys

def nmap_basit(ip):
    try:
        # basic nmap scan (basit nmap taramasi)
        print(f"{ip} adresine basit Nmap taraması başlatılıyor...")
        sonuc = subprocess.run(["nmap", ip], capture_output=True, text=True)
        print("Tarama Sonuçları:")
        print(sonuc.stdout)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def nmap_detayli(ip, parameters):
    try:
        # detail nmap scan (detayli nmpa taramasi)
        print(f"{ip} adresine detaylı Nmap taraması başlatılıyor...")
        # in here we add paramters (kullanicdan aldigimiz parametleleri ekliyoruz)
        komut = ["nmap"] + parameters.split() + [ip]
        sonuc = subprocess.run(komut, capture_output=True, text=True)
        print("Tarama Sonuçları:")
        print(sonuc.stdout)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def dirsearch(ip):
    try:
        # with gobuster we search web directorys (gobuster kullanarak web dizin araması yapıyoruz) 
        print(f"{ip} adresine Dirsearch taraması başlatılıyor...")
        # IP adresinin başına "http://" ekliyoruz
        url = f"http://{ip}"
        
        #  with subprocess we start gobuster (gobuster'i subprocess ile başlatıyoruz)
        subprocess.run(["gobuster", "dir","-u", url ,"-w" , "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"], check=True)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def main():
    # we ask the user which scan he want a use (Kullanıcıya hangi taramayı yapmak istediğini soruyoruz)
    print("Hangi taramayı yapmak istersiniz?")
    print("1. Basit Nmap taraması")
    print("2. Detaylı Nmap taraması (Parametreler siz girin)")
    print("3. Dirsearch taraması (HTTP taraması)")

    secim = input("Seçiminizi yapın (1/2/3): ")

    # we start the scan (islemi baslatiyrouz tarmayi yani)
    if secim == '1':
        ip = input("Taramak istediğiniz IP adresini girin: ")
        nmap_basit(ip)
    elif secim == '2':
        ip = input("Taramak istediğiniz IP adresini girin: ")
        parameters = input("Nmap parametrelerini girin (örneğin: -sV -p 80,443): ")
        nmap_detayli(ip, parameters)
    elif secim == '3':
        ip = input("Taramak istediğiniz IP adresini girin: ")
        dirsearch(ip)
        
        sys.exit(0)  
    else:
        print("Geçersiz seçim! Lütfen 1, 2 veya 3'ü girin.")

if __name__ == "__main__":
    main()

