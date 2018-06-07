FROM ubuntu:rolling  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
RUN apt-get update &&\  
apt-get install -y -q bash wget git openssl ca-certificates dirmngr apt-
transport-https python python3 python3-distutils &&\  
wget "https://bootstrap.pypa.io/get-pip.py" &&\  
python3 get-pip.py &&\  
python get-pip.py &&\  
rm get-pip.py  
CMD ["/bin/bash"]  

