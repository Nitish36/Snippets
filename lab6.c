%{
#include<stdio.h>
int count=0;
%}
op[\+\-\*\/\=]
nop[\,\;]
digit[0-9]
letter[a-zA-Z]
id{letter}+|({letter}{digit})+
nid({digit}{letter})+
%%
("if")|("for")|("int") {printf("Keywords %s",yytext);}
{id} {printf("Identifiers %s",yytext);count++;}
{op} {printf("Operator %s",yytext);}
{nop} {printf("Not an operator %s",yytext);}
{nid} {printf("Not an identifier %s",yytext);}
%%
int yywrap(){}
int main()
{
FILE *fp;
char file[10];
printf("Enter the file name\n");
scanf("%s",file);
fp=fopen(file,"r");
yyin=fp;
yylex();
printf("The no of identifier are %d",count);
return 0;
}
