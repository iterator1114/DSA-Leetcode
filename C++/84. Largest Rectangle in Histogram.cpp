class Solution {
public:
    vector<int> nser(vector<int>arr, int n)
    {
        stack<pair<int,int>> st;
        vector<int>index;
        for(int i=n-1;i>=0;i--)
        {
            while(!st.empty() && st.top().first >=arr[i])
                st.pop();
            if(st.empty())
                index.push_back(n);
            else
                index.push_back(st.top().second);
            st.push({arr[i],i});
        }
        reverse(index.begin(),index.end());
        return index;
    }
    vector<int> nsel(vector<int> arr,int n)
    {
        stack<pair<int,int>> st;
        vector<int> index;
        for(int i=0;i<n;i++)
        {
            while(!st.empty() && st.top().first >=arr[i])
                st.pop();
            if(st.empty())
                index.push_back(-1);
            else
                index.push_back(st.top().second);
            st.push({arr[i],i});

        }
        return index;
    }
    int largestRectangleArea(vector<int>& heights) {
        int n=heights.size();
        vector<int> l=nsel(heights,n);
        vector<int> r=nser(heights,n);
        vector<int> v;
        int m=INT_MIN;
        for(int i=0;i<n;i++)
        {
            v.push_back(heights[i]*(r[i]-l[i]-1));
            if(v[i]>m)
                m=v[i];
        }
        return m;
        
    }
};
