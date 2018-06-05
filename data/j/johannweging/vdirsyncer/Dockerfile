FROM johannweging/base-alpine:latest  
  
RUN set -x \  
&& apk add --update --no-cache python3 bash \  
&& pip3 install vdirsyncer  
  
RUN set -x \  
&& adduser -D -H vsyncer  
  
ADD rootfs /  
  
RUN set -x \  
&& chmod +x /etc/periodic/15min/job \  
&& chmod +x /run.sh  
  
CMD ["/run.sh"]  

