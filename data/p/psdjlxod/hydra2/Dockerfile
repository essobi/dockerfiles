FROM psdjlxod/gcc  
ADD . /tmp/hydra  
WORKDIR /tmp/hydra  
RUN ["gcc","single.c","-o/bin/lcurl-single","-lcurl"]  
RUN ["gcc","multi.c","-o/bin/lcurl-multi","-lcurl"]  
RUN ["./configure"]  
RUN ["make"]  
RUN ["mv", "hydra", "/usr/bin/"]  
RUN ["rm", "-rf", "/tmp/hydra"]  

