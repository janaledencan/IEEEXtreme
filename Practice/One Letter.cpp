#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int n;
vector<string> words;

void read() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string word;
        cin >> word;
        words.push_back(word);
    }
}

int main() {
    read();
    
    string res;
    for (auto& word : words) {
        char smallestLetter = word[0];
        for (auto letter : word) {
            smallestLetter = min(smallestLetter, letter);
        }
        res += smallestLetter;
    }
    sort(res.begin(), res.end());
    cout << res << "\n";
}