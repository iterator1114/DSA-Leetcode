class Solution {
public:
    int minDistance(string s, string t) {
        int count[s.length()+1][t.length()+1];
        int m=s.length();
        int n=t.length();
        for(int i=0;i<m+1;i++)
        {
            for(int j=0;j<n+1;j++)
            {
                if(i==0)
                count[i][j]=j;
                if(j==0)
                count[i][j]=i;
            }
        }
        for(int i=1;i<m+1;i++)
        {
            for(int j=1;j<n+1;j++)
            {
                if(s[i-1]==t[j-1])
                count[i][j]=count[i-1][j-1];
                else
                count[i][j]=1+min(count[i-1][j],min(count[i-1][j-1],count[i][j-1]));
                
            }
        }
        return count[m][n];
        
    }
};
