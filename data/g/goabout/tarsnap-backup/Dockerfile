FROM python:2.7-alpine  
  
MAINTAINER Go About <tech@goabout.com>  
  
ENV CONSUL_VERSION=0.9.2  
RUN apk add --no-cache tarsnap openssh-client && \  
pip install crython six && \  
mkdir /backup /var/cache/tarsnap && \  
rm -rf /tmp/tarsnap-key.asc /var/lib/apt/lists/*  
  
ADD
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
/tmp/consul.zip  
RUN unzip /tmp/consul.zip && \  
mv consul /usr/local/bin && \  
rm /tmp/consul.zip  
  
COPY tarsnap.conf /etc/tarsnap/tarsnap.conf  
COPY scheduler.py /usr/local/bin/scheduler  
  
VOLUME /var/cache/tarsnap  
  
CMD ["scheduler"]  

