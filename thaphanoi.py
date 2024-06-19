n = int(input('nhập số dĩa:'))
def thaphanoi(n, cột_bắt_đầu, cột_đích, cột_trung_gian):
  if n == 1:
    print("Di chuyển dĩa 1 từ cột",cột_bắt_đầu,"sang cột",cột_đích)
    return
  thaphanoi(n-1, cột_bắt_đầu, cột_trung_gian, cột_đích)
  print ("Di chuyển dĩa ",n,"từ cột",cột_bắt_đầu,"sang cột",cột_đích)
  thaphanoi(n-1, cột_trung_gian, cột_đích, cột_bắt_đầu)
print(thaphanoi(n,"gốc","cuối","trung gian"))
