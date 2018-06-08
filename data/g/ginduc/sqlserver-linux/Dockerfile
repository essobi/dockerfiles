FROM microsoft/mssql-server-linux:rc1  
MAINTAINER gian@dynamicobjx.com  
  
COPY . /usr/src/db  
WORKDIR /usr/src/db  
  
ENV ACCEPT_EULA Y  
EXPOSE 1433  
CMD /bin/bash ./entrypoint.sh  
  

