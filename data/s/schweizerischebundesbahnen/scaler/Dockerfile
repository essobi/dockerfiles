FROM alpine  
MAINTAINER Simon Erhardt <simon.erhardt@sbb.ch>  
  
RUN apk add --update \  
tini \  
nodejs-lts \  
python \  
make \  
g++ \  
&& rm -rf /var/cache/apk/*  
  
COPY app /opt/docker-autoscale  
RUN cd /opt/docker-autoscale && npm install  
  
RUN apk del python \  
make \  
g++  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
VOLUME ["/opt/docker-autoscale/config"]  
  
COPY run.sh /opt/docker-autoscale/run.sh  
RUN chmod +x /opt/docker-autoscale/run.sh  
  
CMD ["/opt/docker-autoscale/run.sh"]  

