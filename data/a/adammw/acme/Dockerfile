FROM golang:1.5  
RUN apt-get update && apt-get install -y --no-install-recommends git libcap-
dev  
RUN groupadd -r acmetool && useradd -r -g acmetool acmetool  
  
RUN curl -o /usr/local/bin/gosu -SL
'https://github.com/tianon/gosu/releases/download/1.0/gosu' \  
&& chmod +x /usr/local/bin/gosu  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENV ACMETOOL_VERSION=641ffc98a9091671c0e4b27fbe49e7a5de6172a9  
  
RUN git clone https://github.com/hlandau/acme /src && \  
cd /src && \  
git checkout -q "$ACMETOOL_VERSION" && \  
git status && \  
make && \  
rm -rf /src  
  
VOLUME ["/var/lib/acme"]  
CMD ["/go/bin/acmetool"]  
ENTRYPOINT ["/entrypoint.sh"]  

