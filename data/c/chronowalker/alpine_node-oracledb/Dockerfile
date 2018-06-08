FROM node:8.10.0-alpine  
MAINTAINER Koji Carvalho <stylethewalker@gmail.com.br>  
  
ADD ./libs/*.zip /tmp/  
  
RUN apk update && apk upgrade \  
&& apk add --no-cache alpine-sdk python unzip git \  
&& mkdir /opt/oracle \  
&& unzip /tmp/instantclient-basic-linux.x64-11.2.0.4.0.zip \  
&& unzip /tmp/instantclient-sdk-linux.x64-11.2.0.4.0.zip \  
&& mv instantclient_11_2 /opt/oracle/instantclient \  
&& ln -s /opt/oracle/instantclient/libclntsh.so.11.1
/opt/oracle/instantclient/libclntsh.so \  
&& export LD_LIBRARY_PATH=/opt/oracle/instantclient:$LD_LIBRARY_PATH \  
&& export OCI_LIB_DIR=/opt/oracle/instantclient \  
&& export OCI_INC_DIR=/opt/oracle/instantclient/sdk/include \  
&& npm i -g yarn  

