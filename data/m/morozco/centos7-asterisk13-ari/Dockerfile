FROM centos  
MAINTAINER Miguel Cortes <miguel.cortes@decameron.com>  
#Se actualiza y se installa wget  
RUN yum update -y && yum install -y wget  
#Se descarga asterisk  
RUN cd /usr/src && wget
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-13-current.tar.gz  
RUN cd /usr/src && tar -zxvf /usr/src/asterisk-13-current.tar.gz && cd
/usr/src/asterisk-13.*  
#Se instalan dependencias  
RUN yum install -y gcc gcc-c++ ncurses-devel uuid-devel libuuid-devel jansson-
devel libxml2-devel sqlite-devel  
#Se descarga compilador  
RUN yum install -y make  
#RUN cd /usr/src && make menuselect  
#Se compila e instala asterisk con sus ejemplos  
RUN cd /usr/src/asterisk-13.* && ./configure && make && make install && make
samples  
#Congigurar linker dinamico  
RUN ldconfig  
#Descargar y descomprimir node.js  
RUN wget http://nodejs.org/dist/v0.10.30/node-v0.10.30.tar.gz && tar xzvf
node-v*  
#Instalar node.js  
RUN cd node-v* && ./configure && make && make install  
#Instalar paquete ws de node  
RUN npm install -g wscat  
#Instalar curl  
RUN yum install -y curl  
#Copiar los archivos de configuracion http.conf, ari.conf y extensions.conf
para hola mundo de ARI  
COPY ari.conf /etc/asterisk/  
COPY http.conf /etc/asterisk/  
COPY extensions.conf /etc/asterisk/  
EXPOSE 8088  
CMD ["/bin/bash"]  

