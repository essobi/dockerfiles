FROM alpine:3.2  
MAINTAINER Mario Marín <mario.marin@scalablepath.com>  
  
RUN apk --update add ruby-dev ca-certificates \  
&& rm /var/cache/apk/*  
  
RUN gem install systemd_mon mail slack-notifier hipchat systemd_mon --no-ri
--no-rdoc  
  
ENTRYPOINT ["systemd_mon"]  

