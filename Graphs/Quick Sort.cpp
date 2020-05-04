#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

int partition(int arr[],int low,int high)
{
     int pivot = arr[high];
     int i = low-1;
     for(int j = low;j<high;j++)
          if(arr[j]<pivot)
               swap(arr[++i],arr[j]);
     swap(arr[i+1],arr[high]);
     return i+1;
}
void quicksort(int arr[],int low,int high)
{
     if(low<high)
     {
          int pi = partition(arr,low,high);
          quicksort(arr,low,pi-1);
          quicksort(arr,pi+1,high);
     }
}

int main()
{
     int T = 12;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(QSort).csv");
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
          quicksort(arr,0,N-1);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}
