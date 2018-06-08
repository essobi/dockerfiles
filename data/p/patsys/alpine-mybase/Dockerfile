FROM alpine:latest  
MAINTAINER Patrick Weber <pat.weber91@gmail.com>  
COPY update.sh /etc/  
COPY start /etc/  
RUN apk update \  
&& apk upgrade \  
&& rm -rf /var/cache/apk/*  
RUN chmod u+x /etc/update.sh  
RUN chmod ugo+x /etc/start  
RUN mkdir -p /etc/my_init.d  
RUN mkdir -p /etc/my_update  
RUN echo "#!/bin/sh" > /etc/my_update/empty  
CMD ["/etc/start"]  

