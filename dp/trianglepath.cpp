#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>

#define endl '\n'
#define fastio() ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define MAX 101
using namespace std;

int c;
int n;
int cache[MAX][MAX];
int triangle[MAX][MAX];


//dp(r, c) = max(dp(r+1, c), dp(r+1, c+1)) + triangle(r, c)
int maxPath(int r, int c)
{
    int &ret = cache[r][c];
    if(ret != 0)
        return ret;

    if(r == n-1)
        return triangle[r][c];
    
    return ret = max(maxPath(r+1, c), maxPath(r+1, c+1)) + triangle[r][c]; 
    
}

int main(int argc, char* argv[])
{
    
    fastio();
    cin >> c;
    while(c--)
    {
        cin >> n;
        memset(cache, 0, sizeof(triangle));
        for(int i =0; i <n; i++)
        {
            for(int j = 0 ; j <= i; j++)
            {
                cin >> triangle[i][j];
            }
        }
        cout << maxPath(0, 0) << endl;
    }
    
    return 0;
}
