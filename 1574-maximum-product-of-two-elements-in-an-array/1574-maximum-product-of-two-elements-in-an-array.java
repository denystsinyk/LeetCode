class Solution {
    public int maxProduct(int[] nums) {
        int biggest = -1;
        int secondBiggest = -1;

        for (int i = 0; i < nums.length; i++){
            if (nums[i] > biggest){
                secondBiggest = biggest;
                biggest = nums[i];
            } else if (nums[i] > secondBiggest){
                secondBiggest = nums[i];
            }
        }

        return ((biggest-1)*(secondBiggest-1));
    }
}