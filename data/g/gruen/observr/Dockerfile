FROM docker:1.13.1  
RUN apk --update upgrade && \  
apk add \  
ruby \  
ruby-irb \  
ruby-rdoc \  
libnotify \  
inotify-tools && \  
gem install observr && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
ENTRYPOINT [ "observr" ]  

