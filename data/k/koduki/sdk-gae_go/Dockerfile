FROM debian  
  
ENV GAE_SDK_URL https://storage.googleapis.com/appengine-
sdks/featured/go_appengine_sdk_linux_amd64-1.9.35.zip  
ENV GO_SDK_URL https://storage.googleapis.com/golang/go1.6.2.linux-
amd64.tar.gz  
  
# Base settings  
RUN apt-get update && apt-get install -y wget unzip python git && rm -rf
/var/lib/apt/lists/*  
  
# Install Google App engine with golang  
RUN wget -O tmp.zip ${GAE_SDK_URL} && unzip tmp.zip -d /opt/ && rm tmp.zip  
  
# Install golang  
RUN wget -O - ${GO_SDK_URL}|tar xfvz - -C /usr/local/  
  
ENV GOROOT /usr/local/go  
ENV GOPATH $HOME/go  
ENV PATH $GOROOT/bin:$GOPATH/bin:/opt/go_appengine/:$PATH  
  
RUN go get github.com/gin-gonic/gin

