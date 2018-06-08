FROM alpine:edge  
  
# Setup environment variables  
ENV HOME=/root \  
LANG=en_HK.UTF-8 \  
LANGUAGE=en_HK.UTF-8 \  
LC_ALL=en_HK.UTF-8 \  
TZ=Asia/Hong_Kong  
  
WORKDIR $HOME  
# setup timezone  
RUN apk --no-cache --update --upgrade add tzdata \  
&& cp /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone  
  
RUN apk --no-cache --update add supervisor  
  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

