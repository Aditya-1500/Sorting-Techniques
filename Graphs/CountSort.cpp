#include<iostream>
#include<fstream>
#include<time.h>
#include<bits/stdc++.h>
using namespace std;

void countSort(int arr[],int n)
{
    int max = *max_element(arr, arr+n);
    int min = *min_element(arr, arr+n);
    int range = max - min + 1;

    vector<int> count(range), output(n);
    for(int i = 0; i < n; i++)
        count[arr[i]-min]++;

    for(int i = 1; i < count.size(); i++)
           count[i] += count[i-1];

    for(int i = n-1; i >= 0; i--)
    {
         output[ count[arr[i]-min] -1 ] = arr[i];
              count[arr[i]-min]--;
    }

    for(int i=0; i < n; i++)
            arr[i] = output[i];
}

int main()
{
     int T = 10;
     ifstream inputs("Test Cases.txt");
     ofstream NT("Results(CSort).csv");
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
          countSort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}



