FROM alpine:latest  
  
MAINTAINER Micah Hausler, <hausler.m@gmail.com>  
  
RUN apk add -U wget  
  
ENV VERSION 0.5.1  
ENV DOWNLOAD_URL_BASE https://releases.hashicorp.com/vault/${VERSION}/  
ENV DOWNLOAD_FILE vault_${VERSION}_linux_amd64.zip  
ENV DOWNLOAD_URL $DOWNLOAD_URL_BASE$DOWNLOAD_FILE  
  
ADD $DOWNLOAD_URL /tmp  
ADD verify.sh /tmp  
WORKDIR /tmp  
  
RUN unzip /tmp/$DOWNLOAD_FILE \  
&& mv /tmp/vault /usr/local/bin/vault  
  
EXPOSE 8200  
ENTRYPOINT ["/usr/local/bin/vault"]  
CMD ["server", "-dev"]  

