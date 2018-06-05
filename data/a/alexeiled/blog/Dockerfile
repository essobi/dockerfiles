FROM alpine:3.4  
MAINTAINER Alexei Ledenev <alexei.led@gmail.com>  
  
ENV HUGO_VERSION=0.16  
RUN apk add --update curl openssl ca-certificates && rm /var/cache/apk/*  
  
RUN curl -L --progress-bar
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-64bit.tgz
| tar xvz  
  
RUN mv /hugo /usr/bin/hugo  
  
RUN mkdir -p /src /output  
  
COPY . /src/  
COPY ./run.sh /run.sh  
  
RUN chmod +x /run.sh  
  
WORKDIR /src  
CMD ["/run.sh"]  
  
EXPOSE 1313  

