//Program to implement Heap Sort
#include<iostream>
#include<fstream>
#include<time.h>

using namespace std;

void heapify(int arr[],int n,int i)
{
     int largest = i;
     int l = 2*i;
     int r = 2*i+1;
     if(l<n && arr[l]>arr[largest])
          largest = l;
     if(r<n && arr[r]>arr[largest])
          largest = r;
     if(largest!=i)
     {
          swap(arr[i],arr[largest]);
          heapify(arr,n,largest);
     }
}

void heapsort(int arr[],int n)
{
     for(int i=n/2-1;i>=0;i--)
          heapify(arr,n,i);
     for(int i=n-1;i>=0;i--)
     {
          swap(arr[0],arr[i]);
          heapify(arr,i,0);
     }
}

int main()
{
     int T = 10;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(HSort).csv");
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
          heapsort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}
