FROM golang:1.8  
  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
alien \  
libaio1 \  
postfix \  
mailutils  
  
COPY ./oracle_client /oracle-client  
  
RUN alien -i /oracle-client/oracle-
instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm && \  
alien -i /oracle-client/oracle-
instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm && \  
alien -i /oracle-client/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm  
  
ENV LD_LIBRARY_PATH /usr/lib/oracle/12.2/client64/lib/  
ENV PKG_CONFIG_PATH /oracle-client/  
  
RUN rm -r -f /oracle-client/oracle-
instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm && \  
rm -r -f /oracle-client/oracle-
instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm && \  
rm -r -f /oracle-client/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm  
  
COPY ./postfix_main.cf /etc/postfix/main.cf  

