#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

void SSort(int arr[],int N)
{
     for(int i=0;i<N;i++)
     {
          int minM = arr[i];
          int idx = i;
          for(int j=i+1;j<N;j++)
               if(arr[j]<minM)
               {
                    minM = arr[j];
                    idx = j;
               }
          swap(arr[idx],arr[i]);
     }
}

int main()
{
     int T = 12;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(SSort).csv");
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
          SSort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}

