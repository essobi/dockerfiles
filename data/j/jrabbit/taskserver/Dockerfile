FROM debian:stretch  
MAINTAINER Jack Laxson <jackjrabbit@gmail.com>  
  
RUN apt-get update && apt-get install -y taskd gnutls-bin netcat && apt-get
clean  
  
ENV TASKDDATA=/var/lib/taskd  
  
WORKDIR /var/lib/taskd  
  
RUN rm config  
  
COPY entrypoint.sh /bin/  
  
ENV TAGNAME=v0.0.3  
ADD https://github.com/jrabbit/taskd-client-
go/releases/download/$TAGNAME/taskd-client /bin/  
  
RUN chmod +x /bin/taskd-client  
  
# do it live  
EXPOSE 53589  
VOLUME /var/lib/taskd  
  
# to find the volume: `docker inspect --format='{{.Volumes}}'`  
ENTRYPOINT ["/bin/entrypoint.sh"]  
CMD ["server"]  
HEALTHCHECK \--interval=5m CMD taskd-client --norc --cacert pki/ca.cert.pem
--certificate pki/client.cert.pem --key pki/client.key.pem --insecure
healthcheck  

