FROM ubuntu:17.04  
# Install wget (used to pull down beta release of mysqlbeat)  
RUN sed -i -re 's/([a-z]{2}\\.)?archive.ubuntu.com|security.ubuntu.com/old-
releases.ubuntu.com/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y git golang golang-glide  
  
RUN mkdir -p ~/.go/src/github.com/adibendahan && \  
export GOPATH=/root/.go && export GOROOT=/usr/lib/go-1.7/ && \  
cd ~/.go/src/github.com/adibendahan && \  
git clone https://github.com/adibendahan/mysqlbeat && cd mysqlbeat && git
checkout 1.0.0 && \  
glide update --no-recursive && \  
make && \  
cp mysqlbeat /usr/bin/  
WORKDIR /root  
  
COPY ./mysqlbeat.yml /usr/bin  
  
RUN cp -rf ~/.go/src/github.com/adibendahan/mysqlbeat/etc /root  
  
# A clean-up step may be good here  
ENTRYPOINT ["/usr/bin/mysqlbeat", "-e"]

