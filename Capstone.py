from datetime import date
from os import system, name
import os
from time import sleep

def viewPasien() :
    print('\nDaftar Pasien\n')
    print('ID\t| Nama Pasien\t\t| Dokter Spesialisasi   | Jadwal Kunjungan Selanjutnya')
    for key, value in listPasien.items():
        print(key, '\t| ',listPasien[key]['Nama'], '\t\t| ',listPasien[key]['Dokter'], '\t\t| ',listPasien[key]['lastCheckup'], '\t| ',listPasien[key]['nextCheckup'] )
    sleep(3)
    os.system('cls')

def addPasien():
    print('\n---- \t PENDAFTARAN PASIEN BARU \t \n Biaya pendaftaran = Rp 50.000,-')
    daftar=str(input('Lanjut Pembayaran (y/n): '))
    if daftar!='y':
        return
    else :
        global totalBelanja
        totalBelanja += 50000
        newName=str(input('Nama Pasien :\n\t'))
        newDoctor=str(input('Dokter Spesialisasi :\n\t'))
        newPasienID=str('P'+ str(int(maxID[1:])+1).rjust(3, "0"))
        listPasien[newPasienID]={'Nama' : newName,'Dokter': newDoctor,'lastCheckup' : '-', 'lastBill': 0, 'nextCheckup' : '-'}

def checkID(noMenu):
    viewPasien()
    IDPasien = input('No. Pilihan : ').upper()
    if IDPasien in listPasien :
        if noMenu=='3':
            del listPasien[IDPasien]
        else:
            editConsultation(IDPasien)
    else :
        print('Pilihan tidak tersedia\n\n')
    viewPasien() #check
    
def editConsultation(IDPasi):
    print('''\n\tPilih ID Pasien yang akan diubah/ditambah jadwal konsultasi
            Dokter Umum selalu tersedia Senin - Minggu , pukul 08.00-16.00 - Biaya Konsultasi RP 100.000,-
            Dokter Spesialist tersedia sesuai jadwal dokter - Biaya Konsultasi Rp 150.000,- 
          
          ''')
    updateDoctor=(str(input('Input dokter yang diinginkan: \n\t '))).upper()
    print('Jadwal Kunjungan Selanjutnya :'+ IDPasi)
    updtSchedule=''
    while updtSchedule=='' or date(newYear, newMonth, newDate) < date.today():
        newDate=int(input('\tTanggal : '))
        newMonth =int(input('\tBulan : '))
        newYear =int(input('\tTahun : '))
        try: 
            updtSchedule=date(newYear, newMonth, newDate)
        except:
            print("Input tanggal salah")
        if updtSchedule<date.today():
            print('tanggal harus lebih dari hari ini ')
    listPasien[IDPasi]['nextCheckup']=updtSchedule
    listPasien[IDPasi]['Dokter']=updateDoctor
    global totalBelanja
    if  'UMUM' in updateDoctor:
        totalBelanja += 100000
    else:
        totalBelanja += 150000

def payment():
    TMoney=float(input('JUMLAH UANG PEMBAYARAN = Rp '))
    calcPayment=TMoney-totalBelanja
    while calcPayment<0:
        print('Uang Anda kurang sebesar Rp '+ str(calcPayment*(-1)) )
        TMoney=float(input('JUMLAH UANG PEMBAYARAN = Rp '))+TMoney
        calcPayment=TMoney-totalBelanja
    print('\n=====\tKembali  = Rp '+str(calcPayment) + '\t=====')
    print('\n=====\t TERIMAKASIH \t=====')
    sleep(5)
    os.system('clear')
                
listPasien= {
'P001': {'Nama' : 'Budi', 'Dokter': 'JANTUNG', 'lastCheckup' : '2024-01-11', 'nextCheckup' :  '2024-02-13'}, 
'P002': {'Nama' : 'Ani ', 'Dokter': 'UMUM', 'lastCheckup' : '-', 'nextCheckup' : '-'},
'P003': {'Nama' : 'Jono', 'Dokter': 'GIGI', 'lastCheckup' : '2024-01-10', 'nextCheckup' : '2024-02-15'}, 
'P004': {'Nama' : 'Joko', 'Dokter': 'UROLOGI', 'lastCheckup' : '2024-01-18', 'nextCheckup' : '2024-02-03'}, 
'P005': {'Nama' : 'Siti', 'Dokter': 'ORTOPEDI', 'lastCheckup' : '2024-01-19', 'nextCheckup' : '2024-02-09'}
}
totalBelanja=0

while(True) :
    maxID=(max(listPasien))
    print('''
    ---- Selamat Datang di Data Pasien -----
        List Menu :
        1. Menampilkan Seluruh List Pasirn
        2. Pendaftaran Pasien Baru
        3. Menghapus Jadwal Pasien
        4. Ubah/Tambah Konsultasi
        5. Exit Program \n''')
          
    print('total chart = ' + str(totalBelanja) +' \n \t')
    listMenu = input('''Masukkan angka Menu yang ingin dijalankan: ''')
    
    if listMenu=='1':
        viewPasien()
        
    elif listMenu=='2':
        addPasien()
        viewPasien() # check

    elif listMenu=='3':
        print('\n\tPilih ID Pasien yang akan di hapus\t\n')
        checkID(listMenu)
        
    elif listMenu=='4':
        print('\n\tPilih ID Pasien yang akan diubah/ditambah jadwal konsultasi\t\n')
        checkID(listMenu)
        print('\nTotal belanja = ' + str(totalBelanja)+'\n')
        pembayaran=str(input('Lanjut Pembayaran (y/n): '))
        if pembayaran=='y':
            payment()
            totalBelanja = 0
        else :
            print('pembayaran gagal kembali ke menu utama')
    elif listMenu=='5':
        break
    else :
        print('Pilihan tidak tersedia')