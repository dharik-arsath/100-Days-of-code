/*Mini project of Personal Diary Management by Dharik Arsath,Dhananjeyan, Dheena dhayalan */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/stat.h>
#define VAL 10
void add_record(void);
void delete_record(void);
void view_records(void);
int main()
{
    char ch[15];
    while (1)
    {
    printf("1:   ADD RECORD\n");
    printf("2:   DELETE RECORD\n");
    printf("3:   VIEW RECORD\n");
    printf("4:   EXIT OUT OF THE PROGRAM\n");
    printf("ENTER YOUR CHOICE: ");
    fgets(ch,10,stdin);
    int value = atoi(ch);
    if (value == 1)
        add_record();
    else if (value == 2)
        delete_record();
    else if (value == 3)
        view_records();
    else if (value == 4)
        exit(1);
    else
    {
        printf("-------------------------------------------------------------------------------\n");
        printf("\n\t\t\tNot a valid option...\n\n");
        printf("-------------------------------------------------------------------------------\n");
    }
}
}
void add_record()
{
    FILE *fp;
    char title[82];
    printf("ADD THE TITLE FOR YOUR RECORD:");
    fgets(title,80,stdin);
    title[strlen(title)-1] = '\0';
    fp = fopen(title,"a+");
    if (fp!= NULL)
    {
        printf("\nSUCCESSFULLY OPENED THE FILE YOU HAVE ASKED\n\n");
        printf("\nENTER A MOMENT TO REMEMBER: ");
        char data[2050];
        fgets(data,2048,stdin);
        fputs(data,fp);
        fclose(fp);
        printf("-------------------------------------------------------------------------------\n");
        printf("\n\tYour file is being written succesfully,Press Enter key to continue.\n\n");
        printf("-------------------------------------------------------------------------------\n");
        getchar();
        system("clear");
    }
    else
        printf("\nSORRY");
}
void view_records()
{
    FILE *fp;
    char title[82];
    int bufferlength = 255;
    char buffer[bufferlength];
    printf("\nEnter the title you would like to view: ");
    fgets(title,80,stdin);
    title[strlen(title)-1] = '\0';
    fp = fopen(title,"r");
    if(fp!=NULL)
    {
        system("clear");
        while(fgets(buffer,bufferlength,fp))
	        printf("\n%s\n",buffer);
        printf("-------------------------------------------------------------------------------\n");
        printf("\n\t\t\tPress any key to continue....\n\n");
        printf("-------------------------------------------------------------------------------\n");
        getchar();
        fclose(fp);
    }
    else
    {
        printf("-------------------------------------------------------------------------------\n");
        printf("\n\t\tFILE NOT EXIST IN THE WORKING DIRECTORY...\n\n");
        printf("-------------------------------------------------------------------------------\n");
    }
}

void delete_record()
{
FILE *fp;
char filename[50];
int ret;
printf("\nEnter the file you would like to remove: ");
fgets(filename,48,stdin);
filename[strlen(filename)-1] = '\0';
fp = fopen(filename,"r");
if(fp!=NULL)
{
    ret = remove(filename);
    if(ret==0)
        printf("-------------------------------------------------------------------------------\n");
        printf("\n\t\tSuccessfully deleted the file you have asked...\n\n");
        printf("-------------------------------------------------------------------------------\n");
}
else
{
    printf("-------------------------------------------------------------------------------\n");
    printf("\n\t\t\tFILE NOT EXIST IN THE WORKING DIRECTORY...\n\n");
    printf("-------------------------------------------------------------------------------\n");
}
}