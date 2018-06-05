FROM python:3.5-alpine  
  
COPY run.sh /root/run.sh  
  
RUN apk --update add --virtual build_deps wget ca-certificates build-base
libffi-dev openssl-dev && \  
pip install --upgrade pip && \  
pip install bigchaindb && \  
rm -rf /var/cache/apk/* && \  
chmod +x /root/run.sh  
  
WORKDIR /usr/src/app  
  
CMD [ "/root/run.sh" ]  

