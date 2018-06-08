FROM docker:17.06.2-ce-dind  
  
ENV CLAIR_SCANNER_VERSION=v8  
  
RUN apk add --no-cache bash curl coreutils \  
&& curl -L -o /usr/bin/clair-scanner https://github.com/arminc/clair-
scanner/releases/download/$CLAIR_SCANNER_VERSION/clair-scanner_linux_amd64 \  
&& chmod 777 /usr/bin/clair-scanner  
  
COPY run-clair-scanner.sh /run-clair-scanner.sh  
  
CMD ["/run-clair-scanner.sh"]  

