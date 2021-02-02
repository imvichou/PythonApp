#有序可變動列表list

#直接指定內容的list
grades=[12,60,15,70,90]
print(grades)

#直接取得列表中特定位置的值
grades=[12,60,15,70,90]
print(grades[0])

#取代列表中特定的位置值
grades=[12,60,15,70,90]
grades[0]=1
print(grades[0])

#取得列表中特定範圍的列表，索引1到4，不包含4
grades=[12,60,15,70,90]
print(grades[1:4])

#取代列表中特定範圍
grades=[12,60,15,70,90]
grades[1:4] = []
print(grades)

#列表串接
grades=[12,60,15,70,90]
grades=grades+[12,33]
print(grades)

#取得列表長度
grades=[12,60,15,70,90]
length=len(grades)
print(length)

#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data)

#取得巢狀列表特定位置的值
data=[[3,4,5],[6,7,8]]
print(data[0][0])

#取得巢狀列表特定位置及特定範圍的值
data=[[3,4,5],[6,7,8]]
print(data[0][0:2])

#取代巢狀列表特定位置及特定範圍的值
data=[[3,4,5],[6,7,8]]
data[0][0:2]=[5,5,5]
print(data)

#有序不可變動的列表tuple

#所有操作與list相同唯有使用小括號與內容不可變動
data=(3,4,5)
#data[0]=5 #將會錯誤
print(data)