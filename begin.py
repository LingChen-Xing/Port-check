from datetime import datetime

def compare_files():
    # 读取1.txt的内容（如果存在）
    try:
        with open('1.txt', 'r') as f1:
            set1 = set(f1.read().splitlines())
    except FileNotFoundError:
        set1 = set()

    # 读取2.txt的内容（如果存在）
    try:
        with open('2.txt', 'r') as f2:
            set2 = set(f2.read().splitlines())
    except FileNotFoundError:
        set2 = set()

    # 计算差异：2.txt中有但1.txt中没有的行
    diff = set2 - set1

    # 将差异写入new.txt
    if diff:
        current_time = datetime.now()
        with open('new.txt', 'w') as f_out:
            f_out.write('\n'.join(diff))
        with open('changed.txt', 'a') as f_out:
            f_out.write('\n')
            f_out.write('\n'.join(diff))
            f_out.write('-----'+str(current_time))
            print("端口变动：\n")
            for i in diff:
                print(i)
        with open('1.txt', 'a') as f:
            f.write('\n')
            f.write('\n'.join(diff))
    else:
        print("没有新的端口使用")



if __name__ == "__main__":
    compare_files()