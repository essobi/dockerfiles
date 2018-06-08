FROM alpine  
MAINTAINER Pavel Sterba "email@pavelsterba.com"  
ENV ROBOTS_ROOT /robots  
  
COPY data/enable-robots.sh /enable-robots.sh  
  
RUN apk update && apk upgrade \  
&& apk add ca-certificates python3 py2-pip bash \  
&& rm -rf /var/cache/apk/* \  
&& touch /var/log/robots.log \  
&& mkdir /robots \  
&& chmod +x /enable-robots.sh  
  
CMD ["/enable-robots.sh"]  

