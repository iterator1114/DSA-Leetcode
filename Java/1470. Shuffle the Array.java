class Solution {
    public int[] shuffle(int[] nums, int n) {
        int [] ans = new int[2*n];
        for (int i = 0, j = 0; i < n; i++) {
            ans[j] = nums[i];
            j+=2;
        }
        for (int i = n, j = 1; i < 2*n; i++) {
            ans[j] = nums[i];
            j+=2;
        }
        
        return ans;
    }
}
