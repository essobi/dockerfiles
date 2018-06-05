FROM alpine:latest  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
RUN apk update &&\  
apk add bash git libressl ca-certificates python python3 &&\  
wget "https://bootstrap.pypa.io/get-pip.py" &&\  
python3 get-pip.py &&\  
python get-pip.py &&\  
rm get-pip.py  
CMD ["/bin/bash"]  

