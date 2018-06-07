FROM buildpack-deps:jessie-curl  
  
ENV OAUTH2_PROXY_VERSION=2.0.1  
ENV GOLANG_VERSION=1.7.5  
ENV PATH /opt/oauth2-proxy/bin:$PATH  
  
RUN mkdir -p /opt/oauth2-proxy/bin && mkdir /opt/oauth2-proxy/etc  
ADD oauth2_proxy /opt/oauth2-proxy/bin/oauth2_proxy  
  
CMD oauth2_proxy -config=/opt/oauth2-proxy/etc/config  
  

