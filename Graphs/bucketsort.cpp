#include<iostream>
#include<fstream>
#include<time.h>
#include<bits/stdc++.h>
using namespace std;

void bucketSort(float arr[], int n)
{
    vector<float> b[n];
    for (int i=0; i<n; i++)
    {
       int bi = n*arr[i];
       b[bi].push_back(arr[i]);
    }
    for (int i=0; i<n; i++)
       sort(b[i].begin(), b[i].end());
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < b[i].size(); j++)
          arr[index++] = b[i][j];
}


int main()
{
     int T = 10;
     ifstream inputs("BucketSortTest.txt");
     ofstream NT("Results(BucketSort).csv");
     NT<<"N,Time"<<endl;
     clock_t start,stop;
     while(T--)
     {
          int N;
          inputs>>N;
          float arr[N];
          for(int i=0;i<N;i++)
               inputs>>arr[i];
          start = clock();
          bucketSort(arr,N);
          stop = clock();
          double time_taken = double(stop - start) / double(CLOCKS_PER_SEC);
          NT<<N<<","<<time_taken<<endl;
     }
     return 0;
}

