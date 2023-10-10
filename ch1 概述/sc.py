#encoding=utf-8

import random

member_list = []

//加载文件
def init(file_name):
    global member_info
    with open(file_name, 'r') as member_file: 
        for member_info in member_file:
            member_list.append(member_info.strip())

//随机读取文件中的list[member_no]
def sc():
    member_no = int(random.uniform(0,len(member_list) - 1))
    print (member_list[member_no])

def main():
    init('E:\\python cases\\list of student.txt')  //需要修改学生列表路径
    sc()
        
if __name__ == '__main__':
    main()