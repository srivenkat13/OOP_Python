# class Booking:
#     def __init__(self, bid, tno, bdate, guests, status):
#         self.bookindId = bid
#         self.tableNo = tno
#         self.bookingDate = bdate
#         self.guests = guests
#         self.status = status

#         if status.lower()=="book":
#             self.status= "Booked"
#         elif status.lower()=='reserve':
#             self.status="Reserved"

#     def getTableNo(self,bdate):
#         if self.bdate == bdate and self. status == "Booked":
#             return self.tableNo
#         return -1

#     def updateStatus (self,bdate):
#         bDate = int(self.date[:2])
#         date = int(date[:2])
#         if date == bDate+2 and self.status== "Reserved":
#             self.status= "Canceled"
#         elif date == bDate+1 and self.status=="Booked":
#             self.status = "Closed"


# class Restaurant:
#     def __init__(self, tlist):
#         self.tableList = tlist
#         self.bookingList = []
