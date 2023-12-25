# Parallel_Program_Final_Project
This project we implement the Parallel Radix Sort

## Data
we use the testcases 1-30 from CS542200 2023 HW3.  
The input file contrain the unsorted floating point with binary format.  
(i.e 4 byte for each number)

## Compile
```
nvcc radix_sort -o sort
```

## Run
```
./sort {Number of Data} {Input File} {Output File}
```

## Acknowledgements
Our code is based on 
https://github.com/mark-poscablo/gpu-radix-sort  