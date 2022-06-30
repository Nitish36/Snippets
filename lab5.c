#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
char op[2],arg1[5],arg2[5],result[5];
void main()
{
	FILE *fp1,*fp2;
	int count =1;
	fp1 = fopen("input.txt","r");
	fp2 = fopen("output.txt","w");
	while(!feof(fp1))
	{
		fscanf(fp1,"%s%s%s%s",result,arg1,op,arg2);
		if(arg2[0]=='?' && result[0]=='T')
		{
			fprintf(fp2,"\n LD R0,%s",arg1);
		}
		if(arg1[0]!='T' && arg2[0]!='T' && strcmp(op,"+")==0)
		{
			fprintf(fp2,"\n LD R1,%s",arg1);
			fprintf(fp2,"\n LD R2,%s",arg2);
			fprintf(fp2,"\n ADD R1,R1,R2");
		}
		if(arg1[0]=='+' && arg2[0]=='+' && strcmp(op,'*')==0)
		{
			fprintf(fp2,"\n MULT R1,R1,R0");
		}
		if((strcmp(op,"=")==0) && (arg1[0] == '+') && count==1)
		{
			fprintf(fp2,"\n ST %s, R0",result);
			count++;
		}
	}
	fclose(fp1);
	fclose(fp2);
}
