FROM alpine  
  
ENV MD5_SUM 654afe667c0ad6074330710c5d8b7b22  
  
ENV EMAIL_LIST **None**  
  
RUN apk add --update-cache curl tar  
RUN curl -sL
https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-
amd64.go1.8.1.tar.gz -o /google_auth_proxy.tar.gz  
RUN echo "${MD5_SUM} google_auth_proxy.tar.gz" > google_auth_proxy.md5  
RUN md5sum google_auth_proxy.tar.gz  
RUN md5sum -c google_auth_proxy.md5  
RUN tar --strip-components=1 -zxf google_auth_proxy.tar.gz  
  
COPY run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["-help"]  

