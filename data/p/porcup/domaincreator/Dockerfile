FROM progrium/busybox  
MAINTAINER Huy TA <hlieuta@gmail.com>  
  
ENV VERSION 1.0.0  
# provide /etc/ssl/certs/ca-certificates.crt to container  
RUN opkg-install ca-certificates  
RUN for cert in `ls -1 /etc/ssl/certs/*.crt | grep -v /etc/ssl/certs/ca-
certificates.crt`; do cat "$cert" >> /etc/ssl/certs/ca-certificates.crt; done  
  
ADD bin/domaincreater /app/domaincreater  
RUN chmod u+x /app/domaincreater  
  
COPY docker-entrypoint.sh /app/docker-entrypoint.sh  
RUN chmod u+x /app/docker-entrypoint.sh  
  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["/app/domaincreater"]

