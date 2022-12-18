import os
import time

class antrean :
    def __init__ (self, x = None ) :
        os.system("cls")
        print("=" * 34)
        print("== \tANTREAN SWAB TES \t==")
        print("=" * 34, "\n")
        input("Tekan ENTER untuk memulai program\n")
        os.system("cls")
        x = input("\tJumlah Antrean Maksimal : ")
        self.ukuran = int(x)
        self.sekarang = 0
        self.nama = []
        self.NIK = []

    def menu(self) :
        os.system("cls")
        print("\n\tMENU")
        print("1. Lihat Antrean")
        print("2. Antrean masuk(append)")
        print("3. Jenis Swab")
        print("4. Antrean keluar(pop)")
        print("5. Keluar")
        y = input("\nMasukkan Pilihan : ")
        self.pilih_menu(y)

    def menudua(self):
      os.system("cls")
      print("\n\tJENIS SWAB")
      print("1. Swab PCR Atau Real-time Reverse Transcription Polymerase Chain (RT-PCR)")
      print("2. Rapid Test Antigen-Swab")
      z = input("\nMasukkan Pilihan : ")
      self.pilih_menu_dua(z)


    def jika_kosong(self) :
        if self.sekarang == 0 :
           return True
        else :
           return False
           
    def jika_penuh(self) :
        if self.sekarang == self.ukuran :
           return True
        else :
           return False

    def enqueue(self, nama, NIK) :
        self.nama.append(nama)
        self.NIK.append(NIK)
        self.sekarang = len(self.nama)
        print("Antrian atas Nama ", nama, "Dengan No NIK", NIK, "Berhasil Ditambahkan")
        print("Silahkan Menempati Tempat Duduk Yang Sudah Disediakan")

    def dequeue(self,) :
        dta_nama = self.nama.pop(0)
        dta_NIK = self.NIK.pop(0)
        self.sekarang = len(self.nama)
        self.sekarang - len(self.NIK)
        print("Antrian Atas Nama ", dta_nama, "Dengan No NIK", dta_NIK)
        print("Dipersiahkan Masuk Keruangan")

    def visual_data(self) :
        os.system("cls")
        print("\t\t\tDATA PASIEN SWAB\n")
        for i in range(self.ukuran) :
           print("    [%2d]    "%(self.ukuran-1), end = "")
        print()
        for i in range(self.ukuran) :
           print("===========", end = "")
        print()

        posisi_kosong = self.ukuran - self.sekarang
        for i in range(self.ukuran) : 
           if i < posisi_kosong :
                print(" %10s "%(""), end = "")
           else :
                print(" %10s "%(self.nama[self.ukuran-1-i]), end = "")

        print(">>[NAMA]", end = "")
        print()
        posisi_kosong =self.ukuran - self.sekarang
        for i in range(self.ukuran) :
           if i < posisi_kosong :
                print(" %10s "%(""), end = "")
           else :
                print(" %10s "%(self.NIK[self.ukuran - 1 - i]), end = "")

        print(">>[NIK]", end = "")
        print()

        posisi_kosong = self.ukuran - self.sekarang
        for i in range(self.ukuran) :
           print("===========", end = "")

        print("")
    
    def pilih_menu(self, pilih) :
        if pilih == "1" :
           self.lihat_antrean()
        elif pilih == "2" :
           self.antrean_masuk()
        elif pilih == "3" :
           self.menudua()
        elif pilih == "4" :
           self.antrean_keluar()
        elif pilih == "5" :
           self.keluar_program()
        elif pilih == "" :
           self.menu()
        else :
           print("Maaf Inputan Yang Anda Masukan Salah")
           print("Tekan [ENTER] untuk kembali")
           input("Tekan ENTER untuk kembali")
           self.menu()

    def pilih_menu_dua(self,pilihan):
      if pilihan == "1" :
         self.PCR()
      elif pilihan == "2" :
         self.Antigen()
      else :
           print("Maaf Inputan Yang Anda Masukan Salah")
           print("Mohon Masukkan Kembali Inputan Yang Benar")
           time.sleep(2)
           self.menudua()

    def PCR(self):
      print("="*32)
      print("== Tarif Harga Untuk Swab PCR ==")
      print("== RP 275.000                 ==")
      print("="*32)
      input("Tekan [Enter] Untuk Kembali Ke Halaman Menu")
      self.menu()

    def Antigen(self):
      print("="*36)
      print("== Tarif Harga Untuk Swab Antigen ==")
      print("== RP 99.000                      ==")
      print("="*36)
      input("Tekan [Enter] Untuk Kembali Ke Halaman Menu")
      self.menu()

    def lihat_antrean(self) :
        antrean.visual_data(self)
        input()
        self.menu()

    def antrean_masuk(self) :
        if self.jika_penuh() :
            print("Antrean penuh")
        else :
           nama = input("Masukkan Nama : ")
           NIK = input("Masukkan NIK : ")
           self.enqueue(nama, NIK)
        input()
        self.menu()

    def antrean_keluar(self) :
        if self.jika_kosong() :
           print("Maaf Antrean Saat ini Kosong")
        else :
           self.dequeue()
        input()
        self.menu()

    def keluar_program(self):
        os.system("cls")
        print("="*80)
        print("=== T E R I M A K A S I H  T E L A H  B E R K E N A N  S W A P  D I  S I N I ===")
        print("="*80)
        
if __name__ == "__main__" :
    a = antrean()
    a.menu()