FROM alpine:3.3  
MAINTAINER Bryan Talbot <bryan.talbot@ijji.com>  
WORKDIR /fakes3_data  
VOLUME ["/fakes3_data"]  
EXPOSE 8000  
CMD ["fakes3", "server", "--root", ".", "--port", "8000"]  
  
RUN apk add --no-cache ruby ruby-io-console  
  
RUN gem install fakes3 -v 0.2.3 --no-doc  

