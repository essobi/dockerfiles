FROM alpine:latest  
MAINTAINER Jake Wise <jake.wise@groovycarrot.co.uk>  
  
ENV DESTINATION=/var/www  
  
ADD layer /  
  
RUN chmod +x /start.sh \  
&& apk update \  
&& apk add bash rsync inotify-tools  
  
ENTRYPOINT ["/start.sh"]  

