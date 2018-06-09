FROM alpine:latest  
MAINTAINER Alexandre Dumont <adumont@gmail.com>  
  
RUN apk update && apk add \  
transmission-daemon \  
&& rm -rf /var/cache/apk/* \  
&& sed -i -e "s#^transmission:.*#transmission:x:119:131:Linux
User,,,:/var/lib/transmission:/bin/sh#" /etc/passwd  
  
ADD start.sh /  
  
ENTRYPOINT ["/start.sh"]  
CMD ["--log-info"]  

