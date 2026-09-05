/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* buildArray(int* n, int s, int* returnSize) {
    int *temp=(int *)malloc(sizeof(int)*s);
    for(int i=0;i<s;i++)
    {
        temp[i]=n[n[i]];
    }
    *returnSize=s;
    return temp;
}