FROM hearstat/jenkins-build-base:alpine  
  
MAINTAINER Hearst Automation Team "atat@hearst.com"  
  
RUN apk --update add ruby ruby-rake &&\  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" &&\  
apk --update add --virtual .ruby-builddeps $runDeps \  
build-base \  
linux-headers \  
ruby-dev \  
libxml2-dev &&\  
gem install -N foodcritic &&\  
gem install -N json &&\  
gem install -N rubocop-checkstyle_formatter &&\  
apk del .ruby-builddeps &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /tmp/*  
  
CMD ["/usr/sbin/sshd", "-D"]  

