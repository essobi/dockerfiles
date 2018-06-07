FROM alpine  
LABEL maintainer="rubengomez78@gmail.com"  
RUN apk add --no-cache \  
python3-dev \  
build-base \  
libffi-dev \  
openssl-dev \  
&& rm -rf /var/cache/apk  
RUN pip3 install ansible==2.4.3.0 \  
&& rm -rf /root/.cache  
CMD ["ansible-playbook"]  

