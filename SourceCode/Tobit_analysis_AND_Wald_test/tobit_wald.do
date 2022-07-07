import delimited data.csv, varnames(1) clear   
tobit pd x1-xN,ll(0) ul(3)   
est store m1   
tobit nd x1-xN,ll(-3) ul(0)
est store m2 
suest m1 m2  
testnl [m1_pd]x1=[m2_nd]x1  
testnl [m1_pd]x2=[m2_nd]x2
testnl [m1_pd]x3=[m2_nd]x3
testnl [m1_pd]x4=[m2_nd]x4
testnl [m1_pd]x5=[m2_nd]x5
testnl [m1_pd]x6=[m2_nd]x6
testnl [m1_pd]x7=[m2_nd]x7
testnl [m1_pd]x8=[m2_nd]x8
testnl [m1_pd]x9=[m2_nd]x9
testnl [m1_pd]x10=[m2_nd]x10
testnl [m1_pd]x11=[m2_nd]x11
testnl [m1_pd]x12=[m2_nd]xN
/* 
Reference：https://blog.csdn.net/weixin_39825322/article/details/113034025
