FROM konstruktoid/alpine  
  
LABEL org.label-schema.name="haproxy" \  
org.label-schema.vcs-url="git@github.com:konstruktoid/HAProxy_Build.git"  
  
RUN apk update && \  
apk upgrade && \  
apk --update add haproxy && \  
rm -rf /var/cache/apk/*  
  
COPY ./haproxy.cfg /etc/haproxy/haproxy.cfg  
  
EXPOSE 8080  
CMD ["haproxy", "-db", "-f", "/etc/haproxy/haproxy.cfg"]  

