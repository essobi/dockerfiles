FROM node:8  
LABEL Team PI "pi-team@mn.nl"  
  
RUN apt-get update \  
&& apt-get -y install unzip libaio1 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ./instantclient/*.zip /opt/oracle/  
  
WORKDIR /opt/oracle/  
RUN unzip instantclient-basiclite-linux.x64-12.2.0.1.0.zip && \  
unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip && \  
rm instantclient-*.zip && \  
mv instantclient_12_2 instantclient && \  
ln -s libclntsh.so.12.1 instantclient/libclntsh.so  
WORKDIR /  
  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/oracle/instantclient \  
OCI_LIB_DIR=/opt/oracle/instantclient \  
OCI_INC_DIR=/opt/oracle/instantclient/sdk/include  
  
# Global installation of oracledb with npm seems to have problems with
permissions.  
RUN yarn global add oracledb  
  
CMD ["bash"]  

