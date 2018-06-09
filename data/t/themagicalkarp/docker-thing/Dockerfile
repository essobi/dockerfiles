FROM dockerfile/nodejs  
  
MAINTAINER Robert Sheehy  
  
  
# ----- Install go -----  
WORKDIR /root  
RUN \  
mkdir -p /goroot && \  
curl https://storage.googleapis.com/golang/go1.3.1.linux-amd64.tar.gz | tar
xvzf - -C /goroot --strip-components=1  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
WORKDIR /data  
# ----------  
RUN git clone https://github.com/theMagicalKarp/docker-thing.git  
WORKDIR /data/docker-thing  
RUN git checkout -b test origin/test  
  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/fsouza/go-dockerclient  
  
RUN npm install -g gulp  
RUN npm install  
RUN gulp build  
  
EXPOSE 5000  

