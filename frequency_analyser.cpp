#include<iostream>
#include<vector>
#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;
using namespace std;

vector<int> frequency(string s){
    int key;
    vector<int> freq(26,0);
    for(int i = 0; i < s.size() ; i++){
        key = s[i] - 'A';
        freq[key]+=1;
    }
    return freq;
}

int main(){
    vector<int> freq;
    freq = frequency("HELLO");
    for(int i: freq){
        cout<<i<<'\n';
    }
    return 0;
}