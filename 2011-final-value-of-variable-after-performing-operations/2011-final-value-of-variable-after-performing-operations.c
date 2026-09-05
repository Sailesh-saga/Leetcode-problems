int finalValueAfterOperations(char** o, int s) {
    int X=0;
    for(int i=0;i<s;i++)
    {
        if(o[i][1]=='-')
        {
            X--;
        }
        else
        {
            X=X+1;
        }
    }
    return X;
}