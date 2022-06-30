%{
int cc=0;
%}
%x CMNTML CMNTSL
%%
"/*" {BEGIN CMNTML;cc++;}
<CMNTML>. ;
<CMNTML>\n ;
<CMNTML>"*/" {BEGIN 0;}
"//" {BEGIN CMNTSL;cc++;}
<CMNTSL>. ;
<CMNTSL>\n {BEGIN 0;}
%%
int yywrap(void){}
int main(int argc,char *argv[])
{
if(argc!=3)
{
printf("usage:%s<cat.txt>%s<catout.txt>\n",argv[1],argv[2]);
return 0;
}
yyin = fopen(argv[1],"r");
yyout = fopen(argv[2],"w");
yylex();
}
