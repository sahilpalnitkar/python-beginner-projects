#Reverse digits of int

def main():
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        ret_val=0
        flag=0
        max = 2**31-1
        min = -2**31

        if (x<0):
            flag=1
            x=x*-1
            
        while(x>0):
            r=x%10
            ret_val=ret_val*10+r
            x=x//10
            
        if(ret_val < min or ret_val > max):
            return 0
        
        if(flag==0):
            print ret_val
            return ret_val
        else:
            print ret_val*-1
            return ret_val*-1
        
    reverse(1231231223231)
if __name__ == "__main__":
    main()