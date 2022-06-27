

def my_string(string,substring):
    count=0
    ml=len(string)
    sl=len(sub_string)
    for i in range(ml):
        s=string[i:i+sl]
        if s==sub_string:
            count+=1
    return count
    
string = input().strip()
sub_string = input().strip()
    
count = my_string(string, sub_string)
print(count)
                