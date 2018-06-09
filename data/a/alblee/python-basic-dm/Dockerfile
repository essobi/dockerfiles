# The basic image is centos  
FROM centos:latest  
  
# Author information  
MAINTAINER Alb.Lee  
  
# Copy Some neccesary files to the image  
ADD requirement.txt Python-3.5.2.tgz instantclient-basic-
linux.x64-11.2.0.4.0.zip instantclient-sdk-linux.x64-11.2.0.4.0.zip /opt/  
  
# Install somepackages by yum  
RUN yum update && \  
yum install -y make unzip gcc zlib zlib-devel git openssl openssl-devel
python-setuptools libaio libaio-devel  
  
# Install Python3.5.2 to images  
WORKDIR /opt/Python-3.5.2/  
RUN ./configure && \  
make && \  
make install && \  
rm /usr/bin/python && \  
ln -s /usr/local/bin/python3 /usr/bin/python && \  
ln -s /usr/local/bin/pip3 /usr/bin/pip  
WORKDIR /  
  
# fix the yum bug which is caused by update python to 3.5.2  
RUN sed -i 's/python/python2/' /usr/libexec/urlgrabber-ext-down && \  
sed -i 's/python/python2/' /usr/bin/yum && \  
rm -fr /opt/Python-3.5.2  
  
# Install neccesary part of oracle client for cx_Oracle  
RUN unzip /opt/instantclient-basic-linux.x64-11.2.0.4.0.zip -d /opt/ && \  
unzip /opt/instantclient-sdk-linux.x64-11.2.0.4.0.zip -d /opt/ && \  
rm /opt/instantclient-basic-linux.x64-11.2.0.4.0.zip && \  
rm /opt/instantclient-sdk-linux.x64-11.2.0.4.0.zip && \  
ln -s /opt/instantclient_11_2/libclntsh.so.11.1
/opt/instantclient_11_2/libclntsh.so && \  
echo "export ORACLE_HOME=/opt/instantclient_11_2" > /etc/profile.d/oracle.sh  
ENV ORACLE_HOME=/opt/instantclient_11_2 \  
LD_LIBRARY_PATH=/opt/instantclient_11_2:$LD_LIBRARY_PATH  
  
# Install python packages from the requirement list  
RUN ldconfig && \  
pip install -r /opt/requirement.txt && \  
rm /opt/requirement.txt  

