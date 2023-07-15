#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>

#define endl '\n'
#define fastio() ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define MAX 101
using namespace std;

int c;
string wildcard;
int n;
string str;
int cache[MAX][MAX];

bool match(int w, int s)
{
    int &ret = cache[w][s];
    if(ret != -1)
        return ret;
    
    while(s < str.size() && w < wildcard.size() && (wildcard[w] == '?' || wildcard[w] == str[s]))
    {
        w++;
        s++;
    }
    
    if(w == wildcard.size())
        return ret = s == str.size();

    if(wildcard[w] == '*')
    {
        for(int skip = 0; s +skip <= str.size(); ++skip)
        {
            if (match(w+1, s+skip))
                return ret = true;
        }
    }
    return ret = false;
        

}

int main(int argc, char* argv[])
{
    
    fastio();
    cin >> c;
    while(c--)
    {
        vector<string> ans;
        cin >> wildcard;
        cin >> n;
        for(int i = 0 ; i < n; i++)
        {
            cin >> str;
            memset(cache, -1, sizeof(cache));
            if (match(0, 0))
            {
                ans.push_back(str);
            }
        }
        sort(ans.begin(), ans.end());
        for (auto a : ans)
            cout<<a<<endl;
    }
    
    return 0;
}
