#include<iostream>
#include<fstream>
#include<time.h>
using namespace std;

void Merge(int arr[],int l,int m,int r);
void MergeSort(int arr[],int l,int r)
{
     if(l<r)
     {
          int m = (l+r)/2;
          MergeSort(arr,l,m);
          MergeSort(arr,m+1,r);
          Merge(arr,l,m,r);
     }
}

void Merge(int arr[],int l,int m,int r)
{
     int nL = m-l+1;
     int nR = r-m;
     int L[nL],R[nR];
     int c = 0;
     for(int i=l;i<=m;i++)
          L[c++] = arr[i];
     c = 0;
     for(int i=m+1;i<=r;i++)
          R[c++] = arr[i];
     int p=0,q=0,k=l;
     while(p<nL && q<nR)
     {
          if(L[p]<R[q])
          {
               arr[k++] = L[p];
               p++;
          }
          else
          {
               arr[k++] = R[q];
               q++;
          }
     }
     while(p<nL)
          arr[k++] = L[p++];
     while(q<nR)
          arr[k++] = R[q++];
}

int main()
{
     int T=10;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(MSort).csv");
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
          MergeSort(arr,0,N-1);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}
