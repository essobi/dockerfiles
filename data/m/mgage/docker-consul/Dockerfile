FROM consul:0.7.2  
RUN apk update && \  
apk add build-base ca-certificates bash py-pip libffi-dev python-dev openssl-
dev && \  
pip install credstash && \  
cd /tmp && \  
rm -rf /tmp/build && \  
apk del gnupg openssl && \  
rm -rf /root/.gnupg  
RUN curl https://releases.hashicorp.com/consul-replicate/0.3.1/consul-
replicate_0.3.1_linux_amd64.tgz > consul_replicate.tgz  
RUN tar xvf consul_replicate.tgz  
RUN chmod u+x consul-replicate  
RUN mkdir -p /usr/local/sbin  
RUN mkdir -p /config  
RUN mv consul-replicate /usr/local/sbin/consul-replicate  
ADD bootstrap.sh .  
ENTRYPOINT ["sh","/bootstrap.sh"]  
CMD [""]  

