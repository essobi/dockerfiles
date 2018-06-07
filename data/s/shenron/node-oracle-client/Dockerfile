FROM node:8.11  
RUN apt-get update && apt-get install -y \  
unzip \  
libaio-dev  
  
COPY /conf/oracle /opt/oracle  
  
# Install oracle client dependencies  
RUN cd /opt/oracle && \  
unzip ./instantclient-basic-linux.x64-12.1.0.2.0.zip -d ./unzip && \  
unzip ./instantclient-sdk-linux.x64-12.1.0.2.0.zip -d ./unzip && \  
rm ./instantclient-basic-linux.x64-12.1.0.2.0.zip ./instantclient-sdk-
linux.x64-12.1.0.2.0.zip ./instantclient-sqlplus-linux.x64-12.1.0.2.0.zip &&\  
mv ./unzip/instantclient_12_1 ./unzip/instantclient  
  
# Create environment variables to npm oracle dependencies  
ENV OCI_LIB_DIR="/opt/oracle/unzip/instantclient"  
RUN ln -s $OCI_LIB_DIR/libclntsh.so.12.1 $OCI_LIB_DIR/libclntsh.so  
  
ENV LD_LIBRARY_PATH="/opt/oracle/unzip/instantclient"  
ENV OCI_INC_DIR="$OCI_LIB_DIR/sdk/include"  

