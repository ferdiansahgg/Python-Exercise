lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim","Oscar","Toby"]
friends.extend(lucky_numbers)# menggabungkan 2 list
friends.append("Creed") # menambahkan kata di akhir list
friends.insert(1, "Mirga") #menginsert mirga dan data lainnya akan dikenankan
friends.remove("Oscar") # menghapus Oscar dari list
friends.clear() # mengkosongkan list
friends.sort() # mengurutkan list dengan cara ascending
lucky_numbers.reverse() # untuk mengurut terbalik
#friends.pop()

friends2 = friends.copy() # untuk menyalin nilai friends ke friends2        
print(friends)
print(friends.index("Kevin")) # cara liat kevin ada di index
print(friends.count("Jim")) # menghitung ada bera jumlah jim di list