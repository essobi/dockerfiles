FROM golang:1.6  
  
RUN echo 'deb http://ftp.de.debian.org/debian stretch main contrib non-free'
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -t stretch -y \--no-install-recommends libmapnik-dev vim && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
WORKDIR /usr  
ENV GOPATH /usr  
  
RUN go get -d github.com/herryhou/go-mapnik/mapnik && \  
go get -d github.com/herryhou/go-mapnik/maptiles && \  
cd /usr/src/github.com/herryhou/go-mapnik/mapnik && \  
cp ./configure.bash /tmp && \  
chmod +x /tmp/configure.bash && \  
/tmp/configure.bash  
  
#RUN cd /usr/src/github.com/herryhou/go-mapnik && \  
# go build -a -installsuffix cgo main.go && \  
# mv main /tmp && \  
# chmod +x /tmp/main  
  
#CMD ["/tmp/main"]

