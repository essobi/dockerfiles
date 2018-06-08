FROM python:2.7-alpine  
RUN apk add --update \  
build-base \  
openssh-client \  
libffi-dev \  
openssl-dev \  
&& rm -rf /var/cache/apk/*  
RUN pip install ansible boto six  
RUN mkdir /app  
WORKDIR /app  
COPY ansible-wrap.sh /ansible-wrap.sh  
RUN chmod +x /ansible-wrap.sh  
RUN mkdir -p /etc/ansible  
COPY ansible.conf /etc/ansible/ansible.cfg  
ENTRYPOINT ["/ansible-wrap.sh"]

