FROM alpine  
MAINTAINER Genki Takiuchi <genki@s21g.com>  
  
RUN apk add --update ruby && rm -rf /var/cache/apk/*  
RUN gem install --no-ri --no-rdoc json_pure && gem cleanup  
  
RUN mkdir -p /gantry  
WORKDIR /gantry  
COPY ./client ./server ./  
  
ENTRYPOINT ["./server"]  

