FROM gliderlabs/alpine:3.3  
ENV ROUTE53_UPDATE_FREQUENCY 10800  
RUN apk add --update \  
python \  
py-pip \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
ADD run.sh /run.sh  
  
RUN wget http://github.com/JacobSanford/route-53-dyndns/archive/master.zip &&
\  
unzip master.zip && mv route-53-dyndns-master/* . && \  
pip install -r /app/requirements.txt  
  
CMD ["/run.sh"]  

