FROM braisgabin/tesseract  
  
RUN apt update && \  
apt install -y --no-install-recommends \  
ca-certificates \  
curl \  
g++ \  
gcc \  
git  
  
RUN curl -O https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go*.linux-amd64.tar.gz  
  
ENV GOROOT=/usr/local/go  
ENV GOPATH=/go  
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH  
  
RUN mkdir -p $GOPATH  
  
RUN go get github.com/otiai10/gosseract  
RUN go get github.com/otiai10/mint  
  
RUN go test github.com/otiai10/...  
  

