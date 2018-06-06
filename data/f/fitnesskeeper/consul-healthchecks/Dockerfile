FROM alpine:3.6  
RUN apk -v --update add \  
bash \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
jq \  
curl \  
dumb-init \  
&& \  
pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic && \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
COPY scripts/*.sh /usr/local/bin/  
COPY check_definitions/*.sh /usr/local/bin/check_definitions/  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN mkdir /consul_check_definitions  
#RUN /usr/local/bin/create_check.sh > /consul_check_definitions/docker-
test.json  
VOLUME /root/.aws  
VOLUME /consul_check_definitions  
ENTRYPOINT ["docker-entrypoint.sh"]  

