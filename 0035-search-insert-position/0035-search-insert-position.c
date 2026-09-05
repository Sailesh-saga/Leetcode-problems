int searchInsert(int* n, int s, int t) {
    int index;
    for(int i=0;i<s;i++)
    {
        if(n[i]>=t)
        {
            index=i;
            break;
        }
    }
    return index;

}