FROM python:3  
MAINTAINER 王康 <earl.k.wang@wangk.cn>  
  
COPY run-certbot.sh /root/certbot/run-certbot.sh  
RUN /usr/local/bin/pip install certbot  
ENTRYPOINT bash -c "bash /root/certbot/run-certbot.sh"  

