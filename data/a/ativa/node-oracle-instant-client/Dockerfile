FROM node:8.9.3  
  
RUN mkdir -p /opt/oracle  
  
RUN apt-get update \  
&& apt-get -y install sudo \  
&& apt-get install -y netcat \  
&& sudo apt-get install -y libaio1 libaio-dev \  
&& apt-get install -y build-essential \  
&& apt-get install -y unzip \  
&& apt-get install -y curl \  
&& wget https://github.com/ativainvestimentos/oracle-
instantclient/raw/master/instantclient-basic-linux.x64-12.1.0.1.0.zip \  
&& wget https://github.com/ativainvestimentos/oracle-
instantclient/raw/master/instantclient-sdk-linux.x64-12.1.0.1.0.zip \  
&& wget https://github.com/ativainvestimentos/oracle-
instantclient/raw/master/instantclient-sqlplus-linux.x64-12.1.0.1.0.zip \  
&& unzip instantclient-basic-linux.x64-12.1.0.1.0.zip -d /opt/oracle \  
&& unzip instantclient-sdk-linux.x64-12.1.0.1.0.zip -d /opt/oracle \  
&& unzip instantclient-sqlplus-linux.x64-12.1.0.1.0.zip -d /opt/oracle  
  
ENV LD_LIBRARY_PATH "/opt/oracle/instantclient_12_1"  
RUN sudo sh -c "echo /opt/oracle/instantclient_12_1 >
/etc/ld.so.conf.d/oracle-instantclient.conf"  
RUN sudo ldconfig  

