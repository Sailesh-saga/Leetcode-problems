int search(int* nums, int n, int t) {
   int low=0,high=n-1,index;
   while(low<=high)
   {
    int mid=(low+high)/2;
    if(nums[mid]==t)
    {
        return mid;
    }
    else if(nums[mid]<t)
    {
        low=mid+1;
    }
    else if(nums[mid]>t)
    {
        high=mid-1;
    }
   } 
   return -1;
}