FROM alpine:3.6  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN apk add --no-cache \  
bash \  
ruby \  
ruby-dev \  
build-base \  
sqlite \  
sqlite-dev && \  
gem install --no-rdoc --no-ri bundler json mailcatcher  
  
EXPOSE 1080  
EXPOSE 1025  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

