FROM ubuntu:xenial  
  
RUN apt-get update && apt-get -y install python3 python3-pip build-essential
bzip2 wget curl git make cmake libusb-1.0-0-dev && \  
pip3 install pycryptodome boto3 && \  
wget -nv https://developer.arm.com/-/media/Files/downloads/gnu-
rm/6-2017q2/gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2 && \  
tar -xf gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2 -C /usr/local/ && \  
rm gcc-arm-none-eabi-6-2017-q2-update-linux.tar.bz2 && \  
wget -nv https://bitbucket.org/awslabs/amazon-s3-bitbucket-pipelines-
python/raw/d1a2cd2355813b62621d8fedc9e100acf9adb228/s3_upload.py && \  
mv s3_upload.py /usr/local/bin  
ENV PATH="/usr/local/gcc-arm-none-eabi-6-2017-q2-update/bin:${PATH}"  

