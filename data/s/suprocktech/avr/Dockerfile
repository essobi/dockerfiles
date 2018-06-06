FROM ubuntu:xenial  
  
RUN apt-get update && apt-get -y install python3 python3-pip build-essential
bzip2 wget curl git make cmake libusb-1.0-0-dev && \  
pip3 install pycryptodome boto3 && \  
wget -nv http://www.atmel.com/images/avr8-gnu-
toolchain-3.5.4.1709-linux.any.x86_64.tar.gz && \  
tar -xf avr8-gnu-toolchain-3.5.4.1709-linux.any.x86_64.tar.gz -C /usr/local/
&& \  
rm avr8-gnu-toolchain-3.5.4.1709-linux.any.x86_64.tar.gz && \  
wget -nv https://bitbucket.org/awslabs/amazon-s3-bitbucket-pipelines-
python/raw/d1a2cd2355813b62621d8fedc9e100acf9adb228/s3_upload.py && \  
mv s3_upload.py /usr/local/bin  
ENV PATH="/usr/local/avr8-gnu-toolchain-linux_x86_64/bin:${PATH}"  

