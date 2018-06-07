FROM nlesc/xenon-alpine-base  
MAINTAINER Atze van der Ploeg "a.vanderploeg@esciencecenter.nl"  
RUN apk add --no-cache krb5-server krb5 supervisor && \  
rm -rf /var/cache/apk/*  
  
COPY krb5.conf /etc/krb5.conf  
COPY kadm5.acl /var/lib/krb5kdc/kadm5.acl  
COPY kdb.conf /var/lib/krb5kdc/kdb.conf  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN printf "javagat\njavagat\n" | kdb5_util create -r esciencecenter.nl  
RUN kadmin.local -q "addprinc -pw javagat admin/admin@esciencecenter.nl" &&\  
kadmin.local -q "addprinc -pw javagat xenon@esciencecenter.nl"  
EXPOSE 749 464 88  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

