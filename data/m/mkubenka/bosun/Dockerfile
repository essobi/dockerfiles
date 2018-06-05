# https://github.com/mkuzmin/docker-image-bosun  
FROM debian:jessie  
MAINTAINER Michal Kubenka <mkubenka@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
ca-certificates \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOPATH /go  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
RUN curl -SL https://storage.googleapis.com/golang/go1.7.linux-amd64.tar.gz \  
| tar -xzC /usr/local  
  
RUN mkdir -p $GOPATH/src \  
&& git clone https://github.com/bosun-monitor/bosun $GOPATH/src/bosun.org \  
&& cd $GOPATH/src/bosun.org \  
&& go run build/build.go  
  
WORKDIR /data  
  
VOLUME /data  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8070  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["-h"]  

