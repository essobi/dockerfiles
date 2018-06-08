FROM node:latest  
# 安装依赖  
RUN apt-get update && apt-get install -y python make gcc g++ unzip libaio1  
# 安装node-oracledb  
RUN mkdir /opt/oracle  
COPY packages/instantclient-basic-linux.zip /opt/oracle  
COPY packages/instantclient-sdk-linux.zip /opt/oracle  
RUN cd /opt/oracle && unzip instantclient-sdk-linux.zip && unzip
instantclient-basic-linux.zip && mv instantclient_12_2 instantclient  
RUN cd /opt/oracle/instantclient && ln -s libclntsh.so.12.1 libclntsh.so  
  
RUN touch /etc/ld.so.conf.d/oracle-instantclient.conf  
RUN echo "/opt/oracle/instantclient" >> /etc/ld.so.conf.d/oracle-
instantclient.conf  
RUN ldconfig  
  
RUN export OCI_LIB_DIR=/opt/oracle/instantclient  
RUN export OCI_INC_DIR=/opt/oracle/instantclient/sdk/include  
  
RUN npm install -g nodemon

