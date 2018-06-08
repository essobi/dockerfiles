FROM alpine:3.6  
RUN apk update \  
&& apk add --no-cache rsyslog rsyslog-tls \  
ca-certificates openssl \  
bash \  
mysql-client \  
python py-pip \  
&& update-ca-certificates \  
&& pip install s3cmd python-magic  
  
COPY dockerbuild/rsyslog.conf /etc/rsyslog.conf  
  
RUN wget https://raw.githubusercontent.com/silinternational/runny/0.2/runny -O
/usr/local/bin/runny \  
&& chmod +x /usr/local/bin/runny  
  
COPY application/ /data/  
WORKDIR /data  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["crond -f"]  

