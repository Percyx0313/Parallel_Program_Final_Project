
import os
import glob 
import json
if __name__ == "__main__":
    
    in_format_list=sorted(glob.glob("testcases/*.txt"))
    in_file_list=sorted(glob.glob("testcases/*.in"))
    out_file_list=sorted(glob.glob("testcases/*.out"))
    
    
    time_list=[]
    pass_list=[]
    for i,file_format in enumerate(in_format_list):
        print("Running Test Case {}".format(i+1))
        # read format
        with open(file_format, 'r') as fh:
            format_rawdata=fh.read()
        format_data=json.loads(format_rawdata)
        # execute
        os.system("./sort {} {} {} > temp.out.txt".format(str(format_data['n']),in_file_list[i],"test.out"))
        # compare the output file
        with open('temp.out.txt','r') as fh:
            output=[line.rstrip('\n') for line in fh.readlines()]
            time_list.append(float(output[-2].split()[-1]))
            pass_list.append(output[-3].split()[-1])
        
    # show the evaluate result
    print("The time list")
    print(time_list)
    
    print("The total cost time : {} (ms)".format(sum(time_list)))
    
    print("="*30)
    
    Failure_cases=[]
    for i in range(len(pass_list)):
        if pass_list[i]!='PASS':
            Failure_cases.append(pass_list[i]) 
    if(Failure_cases):
        for case in Failure_cases:
            print(f"testcase {case} Fail")    
    else:
        print("There no Failure Case")
        
                   
    
    
    
        
        
        
    
    
    
    