#include <iostream>
#include <vector>
#include <cstring>

#define endl '\n'
#define fastio ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

using namespace std;

const int MAX = 101;

int board[MAX][MAX];
int dp[MAX][MAX];
int n;

int canJumpToEndPoint(int r, int c)
{
    if (r >= n || c >= n)
        return 0;
    if(r== n-1 && c == n-1)
        return 1;
    
    int &ret = dp[r][c];
    if (ret != -1)
        return ret;

    return ret = canJumpToEndPoint(r+board[r][c], c) || canJumpToEndPoint(r, c + board[r][c]);
}

int main()
{
    fastio
    
    int t;
    cin>> t;
    while(t--)
    {
        cin >> n;
        memset(dp, -1, sizeof(dp));
        for(int i = 0; i < n ; i++)
        {
            vector<int> temp;
            for(int j = 0; j < n; j++)
            {
                cin >> board[i][j];
            }
        }
        string ans = canJumpToEndPoint(0, 0) ? "YES" : "NO";
        cout<<ans<<endl;
    }
    
    return 0;
}
