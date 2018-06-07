FROM alpine:3.6  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& wget https://releases.hashicorp.com/serf/0.8.1/serf_0.8.1_linux_amd64.zip
-O /tmp/serf.zip \  
&& unzip /tmp/serf.zip -d /usr/local/bin/ \  
&& rm /var/cache/apk/*.tar.gz /tmp/serf.zip  
  
COPY join_serf.sh /usr/local/bin/  
COPY dummy.sh /usr/local/bin/  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["dummy.sh"]  

