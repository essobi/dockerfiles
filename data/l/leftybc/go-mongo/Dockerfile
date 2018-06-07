FROM mongo:3.4  
  
RUN apt-get update && apt-get install -y wget make && \  
mkdir -p /go /opt && \  
cd /tmp && \  
wget https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz && \  
tar xzvf go1.8.3.linux-amd64.tar.gz && \  
mv go /opt  
  
ENV GOPATH /go  
ENV GOROOT /opt/go  
ENV PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/go/bin:/go/bin  
  
VOLUME /data/db  
EXPOSE 27017 28017  
  
CMD [ "mongod" ]  

