#include<unistd.h>
#include<fcntl.h>
#include<stdio.h>
int main(int argc, char const *argv[])
{
    int fd = open("test", O_RDONLY);
    printf("%d\n", fd);
    return 0;
}