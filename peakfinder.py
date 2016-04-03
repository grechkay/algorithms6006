import numpy as np
#takes a 2d grid and finds the peak in nlog(n) time

n_rows = 5
n_columns = 10

r = n_rows 
c = n_columns


ex = np.random.random((r,c))

print(ex)

def main_algo(x,t):
    # l is the topmost index
    r_ = x.shape[0]
    current_ = r_ // 2
    c_index = np.argmax(x[current_])
    c_max = x[current_][c_index]
    if r_ == 0:
        return (t,c_index)

    if current_ > 0:
        if c_max < x[current_ -1][c_index]:
            return main_algo(x[:(current_-1)],t)
        
        
    if c_max < x[current_ + 1][c_index]:
        return main_algo(x[(current_+1):],t + current_+ 1)

    return (current_,c_index)



def peak_finder(x):
    #takes a 2d numpy array
    #modifies the shape so that the number of 
    #rows is bigger than the number of columns
    shape_ = x.shape
    r_ = shape_[0]
    c_ = shape_[1]
    trans_ = False
    if r_ < c_:
        x = x.T
        trans_ = True

    ans_ = main_algo(x,0)
    if trans_:
        ans_ = tuple(reversed(ans_))
    return ans_


    
print(peak_finder(ex))
    
            



    
