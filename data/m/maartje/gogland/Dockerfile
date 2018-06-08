FROM maartje/desktop-base  
  
ENV version=172.3968.45  
ENV GO_VERSION 1.9  
ENV GOPATH /root/go  
ENV GOROOT /usr/local/go  
  
# add git and curl  
RUN apt-get update && apt-get install -y git curl  
  
# Add go, duh  
RUN curl -fSL "https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz" | tar
xzC /usr/local  
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin  
  
RUN wget https://download.jetbrains.com/go/gogland-${version}.tar.gz &&\  
tar -xzf gogland-${version}.tar.gz &&\  
rm -f gogland-${version}.tar.gz  
  
CMD Gogland-${version}/bin/gogland.sh

