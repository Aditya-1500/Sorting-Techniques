#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

void BubbleSort(int arr[],int N)
{
     for(int i=0;i<N;i++)
          for(int j=0;j<N-i-1;j++)
               if(arr[j]>arr[j+1])
                    swap(arr[j],arr[j+1]);
}

int main()
{
     int T = 10;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(BSort).csv");
     NT<<"N,Time"<<endl;
     clock_t start,stop;
     while(T--)
     {
          int N;
          inputs>>N;
          int arr[N];
          for(int i=0;i<N;i++)
               inputs>>arr[i];
          start = clock();
          BubbleSort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}

