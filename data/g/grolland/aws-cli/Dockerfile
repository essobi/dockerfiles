FROM alpine:3.6  
RUN apk -v --update add \  
bash \  
python \  
py-pip \  
groff \  
less \  
mailcap \  
&& \  
pip install --upgrade awscli==1.11.188 s3cmd==2.0.1 python-magic awscli-local
&& \  
apk -v --purge del py-pip && \  
rm /var/cache/apk/*  
VOLUME /root/.aws  
VOLUME /build  
WORKDIR /build  
#ENTRYPOINT ["aws"]  

