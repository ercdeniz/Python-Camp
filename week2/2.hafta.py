import os
students = []

# Konsolu temizleme


def clear():
    if os.name == 'nt':
        _ = os.system('cls')

# Kullanıcıdan öğe alma


def giveStudent():
    name = input("Öğrencinin ismini giriniz : ")
    surname = input("Öğrencinin soyismini giriniz : ")
    if name.isalpha() and surname.isalpha():
        return (name.title() + " " + surname.title()).strip()

# Listedeki tüm öğelerin listelenmesi


def getall():
    j = 1
    if not len(students) == 0:
        for i in range(len(students)):
            print(f"Öğrenci {j}: " + str(students[i]))
            j += 1
    else:
        clear()
        print("Öğrenci Yok!")

# Listedeki öğenin index sırası + 1


def giveStudentNumber():
    nameSurname = giveStudent()
    if nameSurname in students:
        clear()
        print(f"Öğrenci Numarası: {students.index(nameSurname)+1}")
    else:
        clear()
        print("İsim Soyisim Boş Geçilemez ve Sadece Harf Kabul Edilir")
        print("Lütfen isimi ve soyisimi şu şekilde giriniz:\nİsim:'    ' (Press Enter)\nSoyisim:'    ' (Press Enter)")
        count = int(input(
            "Öğrenci bulunamadı ne yapmak istersiniz\n1-Tekrar Dene\n2-Çıkış Yap\nSeçim:"))
        while True:
            if count == 1:
                giveStudentNumber()
                break
            elif count == 2:
                print("Öğrenci Bulunamadı")
                break
            else:
                print("Geçersiz Değer Girdiniz!")
                break

# ekleme işlemi


def add():
    nameSurname = giveStudent()
    if not nameSurname == "" and not nameSurname == None:
        clear()
        print("Öğrenci Eklendi: " + str(nameSurname))
        return students.append(nameSurname)
    else:
        clear()
        print("İsim Soyisim Boş Geçilemez ve Sadece Harf Kabul Edilir")
        print("Lütfen isimi ve soyisimi şu şekilde giriniz:\nİsim:'    ' (Press Enter)\nSoyisim:'    ' (Press Enter)")
        count = int(input(
            "Öğrenci Eklenemedi ne yapmak istersiniz\n1-Tekrar Dene\n2-Çıkış Yap\nSeçim:"))
        while True:
            if count == 1:
                add()
                break
            elif count == 2:
                print("Öğrenci Eklenemedi")
                break
            else:
                print("Geçersiz Değer Girdiniz!")
                break

# Silme işlemi


def remove():
    clear()
    nameSurname = giveStudent()
    if not nameSurname == None and not nameSurname == "":
        if nameSurname in students:
            print("Öğrenci Silindi: "+str(nameSurname))
            return students.remove(nameSurname)
        else:
            clear()
            print("Lütfen Öğrenci İsim Soyismini doğru giriniz \n'İsim: ' \n'Soyisim:'")
            count = int(input(
                "Öğrenci bulunamadı ne yapmak istersiniz\n1-Tekrar Dene\n2-Çıkış Yap\nSeçim:"))
            while True:
                if count == 1:
                    remove()
                    break
                elif count == 2:
                    print("Öğrenci Silinemedi")
                    break
                else:
                    print("Geçersiz Değer Girdiniz!")
                    break
    else:
        clear()
        print("İsim Soyisim Boş Geçilemez ve Sadece Harf Kabul Edilir")
        print("Lütfen isimi ve soyisimi şu şekilde giriniz:\nİsim:'    ' (Press Enter)\nSoyisim:'    ' (Press Enter)")

# Birden fazla ekleme işlemi


def multiAdd():
    count = int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
    index = 0
    while index < count:
        add()
        index += 1

# Birden fazla silme işlemi


def multiRemove():
    count = int(input("Silmek istediğiniz öğrenci sayısını giriniz: "))
    index = 0
    while index < count:
        remove()
        index += 1
<<<<<<< HEAD

=======
>>>>>>> e4d493d7ad943ce5edefc6151cf83a37fc8908fc
