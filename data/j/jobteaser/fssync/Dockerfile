FROM alpine:latest  
  
LABEL vendor="JobTeaser" \  
com.jobteaser.version="1.0.0" \  
com.jobteaser.release-date="2018-05-24" \  
maintainer="dev@jobteaser.com"  
  
RUN apk add --no-cache \  
bash \  
inotify-tools \  
rsync  
  
COPY sync.sh .  
  
ENTRYPOINT ["/sync.sh"]  

