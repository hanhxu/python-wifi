# n, m = 0, "abc"
# x, y, z = 0.125, "abc", False
# n = n + 1
# n += 1
# print("n =", n)
# print(f"x = {x:.2f}")   #0.12
# print(f"x = {x:.2%}")   #12.50%
# n = 0
# while n < 5:            #0,1,2,3,4
#     print(n)
#     n += 1
# for i in range(2,6):    #2,3,4,5
#     print(i)
# for i in range(5,1,-2): #5,3
#     print(i)
# for i in range(5):
#     print(i)            #0,1,2,3,4
# print(type(5 / 2), (5 / 2), 5 // 2, -3 // 2)  #double slash round down
# print(int(-3/2), 10 % 3, -10 % 3)             #-1  1

# n, m = 1, 2
# if ((n > 2 and n != m) or n == m):
#     n += 1
    
# a = 0
# while n < 5:
#     print(n)
#     n += 1
    
# import math
# print(math.fmod(-10, 3.2), math.floor(3/2), math.ceil(3/2), math.sqrt(2), math.pow(2,3))
# print(math.pow(2,300) < float("inf"))

# arr = [1,2,3]
# print(arr)                       #1,2,3
# arr.append(4)         
# arr.append(5)
# print(arr)                       #1,2,3,4,5
# print(arr[1:3])                  #2,3
# print(arr[0:5])                  #1,2,3,4,5
# arr.pop()                   
# print(arr)                       #1,2,3,4
# arr.insert(1,7)
# print(arr)                       #1,7,2,3,4
# n = 5
# arr = [1] * n
# print(arr)                       #1,1,1,1,1
# print(len(arr))                  #5
# nums = [1,2,3,4,5,6,7,8,9]
# for n in nums:
#     print(n, end = " ")
# print()
# for i in range(len(nums)):
#     if(i == (len(nums) - 1)):
#         print(nums[i])
#     else:
#         print(nums[i], end = ", ")
        
# #variables num1, num2, str1, str2, sale3, and sale4 are referencing 
# #the same lists initially, but when you perform the zip() operation, 
# #the loop assigns new values to num1, str2, and sale3. reassigns 
# #num1, str2, and sale3 to the individual elements of their respective 
# #lists. This means within the loop, num1 is now an integer, str2 is now 
# #a string, and sale3 is now a float.
# num1 = num2 = [1,2,3,4,5]
# name2 = name1 = ['Albert', 'Jim','Hilbert', 'Abe', 'Mike']
# sale3 = sale4 = [125.25,145.5,250.05,10000.25,115.45]
# for num, name, sale in zip(num1, name2, sale3):
#     print(num, name, sale)
# name1.sort()
# print(name1, name2, '\n', num1, num2, '\n', sale3, sale4)

# name3 = ['Albert', 'Jim','Hilbert', 'Abe', 'Mike', 'Jin']
# name3.sort(key=lambda x: len(x))   #sort by length of name3 element
# print(name3)
# #Sort first by length of names, then alphabetically
# name3.sort(key=lambda x: (len(x), x)) 
# print([i for i in range(5)])
# #2D array, [0]*4 create a list with 4 zeros, outer loop makes 4 such rows.
# arr = [[0] * 4 for i in range(4)]  
# print(arr)
# print(ord("a"), ord("z"), ord("A"), ord("Z"))
# #double ended queue
# from collections import deque
# que = deque()
# que.append(1)       #deque([1])
# que.append(2)       #deque([1,2])
# print(que)
# que.popleft()       #deque([2])
# print(que)
# que.appendleft(1)   #deque([1,2])
# print(que)
# que.pop()           #deque([1])
# print(que)
# #hashset
# mySet = set()
# mySet.add(1)
# mySet.add(5)
# mySet.add(2)
# print(mySet)         #1,2,5--in order
# print(len(mySet))    #3
# print(1 in mySet, 5 in mySet, 3 in mySet) #True, True, False
# mySet.remove(2)
# print(mySet)
# #HashMap(dict)
# myMap = {}
# myMap["alice"] = 88
# myMap["bob"] = 77
# print(myMap, len(myMap), "alice" in myMap) #{'alice': 88, 'bob': 77} 2 True
# myMap["alice"] = 80
# print(myMap)             #{'alice': 80, 'bob': 77}
# myMap.pop("bob")
# print(myMap)             #{'alice': 80}
# myMap = {i: 2*i for i in range(3)}
# print(myMap)             #{0: 0, 1: 2, 2: 4}

# secMap = {'alice': 88, 'bob': 77}
# for key in secMap:
#     print(key, secMap[key])
    
# for val in secMap.values():
#     print(val)
    
#     #tuples are like arrays but immutable-can't modify
#     tup = (1,2,3)
#     print(tup)
#     print(tup[0], tup[-1])
#     #tuple can be used as key for hashMap
#     thirdMap = {(1,2): 3}
#     print(thirdMap[(1,2)])
    
#     mySet = set()
#     mySet.add((1,2))
#     print((1,2) in mySet)
#     #heaps, Min is always at idx 0
#     import heapq
#     minHeap = []
#     heapq.heappush(minHeap,3)
#     heapq.heappush(minHeap,2)
#     heapq.heappush(minHeap,4)
#     print(minHeap[0])
#     while len(minHeap):
#         print(heapq.heappop(minHeap))
        
# def double(arr, val):
#     def helper():
#         #modifying array works
#         #enumerate returns an iterable of tuples, where each 
#         # tuple contains: The index of the element. The 
#         # value of the element at that index.
#         for i, n in enumerate(arr):
#             arr[i] *= 2
#         nonlocal val
#         val *= 2
#     helper()
#     print(arr, val)
# nums = [1,2]
# val = 3
# double(nums, val)

# class MyClass:
#     # Constructor
#     def __init__(self, nums):
#         #create member variables
#         self.nums = nums
#         self.size = len(nums)
#     def getLength(self):
#         return self.size
#     def grtDoubleLength(self):
#         return 2 * self.getLength()

import speedtest
import subprocess
import pandas as pd
import re
from ping3 import ping, verbose_ping
    
    
def test_wifi_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    ping_value = st.results.ping
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping_value} ms")


def wifi_ping_test(host='google.com'):
    response_time = ping(host)
    if response_time:
        print(f"Ping to {host}: {response_time}\t{response_time * 1000:.2f} ms")
    else:
        print(f"Failed to ping {host}")
 
    
    
def get_wifi_signal_strength():
    
    wifi_info = {}
    result = subprocess.run(['netsh', 'wlan', 'show', 'int'], stdout = subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if result.returncode != 0:
        print("Error executing command.")
    else:
        print(output) 
    for line in output.split('\n'):
        if 'description' in line.lower():
            wifi_info['Description'] = line.split(':')[1].strip()
        elif re.search(r"^\s*SSID\s*:\s*(.*)", line.upper()):
            wifi_info['SSID'] = line.split(': ')[1].strip()
        elif 'receive rate' in line.lower():
            wifi_info['Receive rate (Mbps)'] = line.split(':')[1].strip()
        elif 'transmit rate' in line.lower():
            wifi_info['Transmit rate (Mbps)'] = line.split(':')[1].strip()
        elif 'signal' in line.lower():
            wifi_info['Signal'] = line.split(':')[1].strip()         
    return wifi_info


def save_to_excel(wifi_data, filename="wifi_info.xlsx"):
    # Convert wifi_data to DataFrame for easier manipulation
    # Create DataFrame from a list containing an empty dictionary
    dFrame = pd.DataFrame([wifi_data])
    dFrame.to_excel(filename, index=False)
    print(f"Data saved to {filename}")
    
    
test_wifi_speed()
wifi_ping_test()  
wifi_profile = get_wifi_signal_strength()
if wifi_profile:
    save_to_excel(wifi_profile)
else:
    print("Wi-Fi information not found or an error occurred.")