FROM python:2.7.9  
MAINTAINER safezpa safezpa<safezpa@gmail.com>  
  
RUN mkdir -p /opt/oracle  
WORKDIR /opt/oracle/  
RUN apt-get update && apt-get install -y zip && apt-get install -y libaio1 &&
apt-get install -y libaio-dev && pip install --upgrade pip  
COPY instantclient-basic-linux.x64-12.2.0.1.0.zip /opt/oracle/  
COPY instantclient-sdk-linux.x64-12.2.0.1.0.zip /opt/oracle/  
RUN unzip /opt/oracle/instantclient-basic-linux.x64-12.2.0.1.0.zip -d
/opt/oracle/ && unzip /opt/oracle/instantclient-sdk-linux.x64-12.2.0.1.0.zip
-d /opt/oracle/  
RUN echo "export LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2" >>
/etc/profile  
RUN echo "export PATH=/opt/oracle/instantclient_12_2:$PATH" >> /etc/profile  
RUN echo "export ORACLE_HOME=/opt/oracle/instantclient_12_2" >> /etc/profile  
RUN cd /opt/oracle/instantclient_12_2 && cd /opt/oracle/instantclient_12_2 &&
ln -s libclntsh.so.12.1 libclntsh.so && ln -s libocci.so.12.1 libocci.so &&
export PATH=/opt/oracle/instantclient_12_2:$PATH && export
LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2 && export
ORACLE_HOME=/opt/oracle/instantclient_12_2 && python -m pip install cx_Oracle  
RUN rm /opt/oracle/instantclient-basic-linux.x64-12.2.0.1.0.zip
/opt/oracle/instantclient-sdk-linux.x64-12.2.0.1.0.zip  

