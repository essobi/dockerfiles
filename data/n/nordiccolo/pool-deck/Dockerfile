FROM golang:1.10.2  
MAINTAINER Matt Taylor matthew.taylor@nordiccolo.com  
  
RUN CGO_ENABLED=0 GOOS=linux  
  
RUN \  
apt-get update && apt-get upgrade -q -y && \  
git config --global http.https://gopkg.in.followRedirects true && \  
git clone https://github.com/sammy007/open-ethereum-pool.git && \  
cd open-ethereum-pool && make  
  
# Utilities  
RUN apt-get install -y curl  
  
COPY config.json /go/config.json  
  
EXPOSE 8008  
EXPOSE 8080  
EXPOSE 8888  
ENTRYPOINT ["/go/open-ethereum-pool/build/bin/open-ethereum-pool"]  

