FROM haproxy:latest  
LABEL maintainer="Gary A. Stafford <garystafford@rochester.rr.com>"  
ENV REFRESHED_AT 2017-12-02  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install certbot curl vim -y  
  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
EXPOSE 8080 8443 63443  

