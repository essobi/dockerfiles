FROM nginx:stable-alpine  
  
MAINTAINER Digital Backstage "tech@universcine.com"  
ENV CONFD_VERSION "0.11.0"  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
/usr/local/bin/confd  
  
COPY entrypoint.sh /  
COPY etc /etc/confd  
  
RUN chmod +x /usr/local/bin/confd entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

