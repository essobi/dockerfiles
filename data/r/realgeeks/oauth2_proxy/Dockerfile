FROM gliderlabs/alpine:3.1  
ENV OAUTH2_PROXY_VERSION 2.0.1.linux-amd64.go1.4.2  
RUN apk --update add curl  
  
RUN echo
"https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-$OAUTH2_PROXY_VERSION.tar.gz"  
RUN curl -L -o oauth2_proxy.tar.gz
"https://github.com/bitly/oauth2_proxy/releases/download/v2.0.1/oauth2_proxy-$OAUTH2_PROXY_VERSION.tar.gz"
&& tar xzvf oauth2_proxy.tar.gz && cp
oauth2_proxy-$OAUTH2_PROXY_VERSION/oauth2_proxy /bin/ && chmod +x
/bin/oauth2_proxy  
  
CMD ["oauth2_proxy"]  

