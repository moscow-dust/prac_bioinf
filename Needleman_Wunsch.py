import numpy as np
def needle(string1, string2):
    gap = 0
    #создание двумерного массива
    arr = np.array(range((len(string1)+1)*(len(string2)+1))).reshape(len(string1)+1, len(string2)+1)
    #заполнение матрицы
    arr[0,0]=gap
    for j in range(1,(len(string2)+1)):
        arr[0,j] = gap-2
        gap = arr[0,j]
    gap = 0
    for i in range(1,(len(string1)+1)):
        arr[i,0] = gap-2
        gap = arr[i,0]
    string1 = list(string1)
    string2 = list(string2)
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i]==string2[j]:
                mis = 1
                arr[i+1,j+1] = max(arr[i,j+1]-2, arr[i+1, j]-2, arr[i,j]+mis)
            else:
                mis = -1
                arr[i+1,j+1] = max(arr[i,j+1]-2, arr[i+1, j]-2, arr[i,j]+mis)
    #построeние двух последовательностей по матрице и вычисление score
    i = len(string1)-1
    j = len(string2)-1
    back_trace1 = []
    back_trace2 = []
    match=0
    mismatch=0
    gap=0
    while i!=-1 and j!=-2:
        if string1[i]==string2[j]:
            if max(arr[i,j+1]-2, arr[i+1,j]-2)<(arr[i,j]+1):                
                back_trace1.append(string1[i])
                back_trace2.append(string2[j])
                i-=1
                j-=1
                match+=1
            else:
                if arr[i,j+1]-2 >= arr[i+1,j]-2:
                    back_trace1.append(string1[i])
                    back_trace2.append("_")
                    i-=1
                    gap+=1
                elif arr[i,j+1]-2<arr[i+1,j]-2:
                    back_trace1.append("_")
                    back_trace2.append(string2[j])
                    j-=1
                    gap+=1
        else:
            if max(arr[i,j+1]-2, arr[i+1,j]-2)<(arr[i,j]-1):                
                back_trace1.append(string1[i])
                back_trace2.append(string2[j])
                i-=1
                j-=1
                mismatch+=1
            else:
                if arr[i,j+1]-2>=arr[i+1,j]-2:
                    back_trace1.append(string1[i])
                    back_trace2.append("_")
                    i-=1
                    gap+=1
                elif arr[i,j+1]-2<arr[i+1,j]-2:
                    back_trace1.append("_")
                    back_trace2.append(string2[j])
                    j-=1
                    gap+=1
    back_trace1.reverse()
    back_trace2.reverse()
    print("First sequence:", back_trace1)
    print("Second sequence:", back_trace2)
    print("Score:", match-2*gap-mismatch)
    return arr
def main():
    #аминокислотные последовательности белков HBB HBA человека
    string1 = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
    string2 = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKYR"
    print(needle(string1, string2))
main() 
#
