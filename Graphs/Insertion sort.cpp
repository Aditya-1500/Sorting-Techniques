//Program to implement Insertion Sort
#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

void ISort(int arr[],int N)
{
     for(int i=1;i<N;i++)
     {
          int temp = arr[i];
          int j = i-1;
          while(j>=0 && arr[j]>temp)
          {
               arr[j+1] = arr[j];
               j--;
          }
          arr[j+1] = temp;
     }
}

int main()
{
     int T = 10;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(ISort).csv");
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
          ISort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}
