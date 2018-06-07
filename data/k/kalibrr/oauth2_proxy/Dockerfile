FROM ubuntu:xenial AS builder  
  
WORKDIR /opt/oauth2_proxy  
  
RUN apt-get update && apt-get install -y wget  
  
ENV DOCKERIZE_VERSION v0.5.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN wget
https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz && \  
tar xf oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz --strip-components 1 && \  
rm oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz  
  
FROM debian:jessie  
  
RUN apt-get update && apt-get install -y ca-certificates && update-ca-
certificates && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt/oauth2_proxy  
  
COPY \--from=builder /usr/local/bin/dockerize /usr/local/bin/dockerize  
COPY \--from=builder /opt/oauth2_proxy /opt/oauth2_proxy  
  
COPY /templates /templates  
  
EXPOSE 4180  
ENTRYPOINT ["/usr/local/bin/dockerize", "-template",
"/templates/config.tmpl:/opt/oauth2_proxy/config"]  
CMD ["/opt/oauth2_proxy/oauth2_proxy", "-config=/opt/oauth2_proxy/config"]  

