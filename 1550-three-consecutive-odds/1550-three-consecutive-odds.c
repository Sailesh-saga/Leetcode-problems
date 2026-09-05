bool threeConsecutiveOdds(int* n, int s) {
    int c=0;
    for(int i=0;i<s-2;i++)
    {
        if(n[i]%2!=0 && n[i+1]%2!=0 && n[i+2]%2!=0)
        {
            c++;
        }
    }
    return c>0;
}