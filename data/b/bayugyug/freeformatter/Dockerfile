#start  
FROM golang  
  
#auth  
MAINTAINER bayugyug<bayugyug@gmail.com>  
  
#environment  
ENV GOHOME=  
ENV GOPATH=$GOHOME/go  
ENV GOSRC=$GOPATH/src  
ENV PATH=$PATH:$GOPATH/bin  
  
#prepare  
RUN apt-get update -y && apt-get install -y \--no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/* && \  
mkdir -p $GOPATH/bin $GOSRC/github.com/bayugyug && \  
cd $GOSRC/github.com/bayugyug && \  
git clone https://github.com/bayugyug/freeformatter.git && \  
cd $GOSRC/github.com/bayugyug/freeformatter && \  
go get -v && \  
go build -tags netgo -installsuffix netgo -installsuffix cgo -v -ldflags "-s
-w -X main.pBuildTime=`date -u +%Y%m%d.%H%M%S`" . && \  
cd $GOSRC && go install github.com/bayugyug/freeformatter && \  
cd $GOSRC/github.com/bayugyug/freeformatter && \  
cp -f Docker/cleanup.sh $GOPATH/bin/ && \  
chmod +x $GOPATH/bin/* && \  
$GOPATH/bin/cleanup.sh  
  
WORKDIR $GOSRC/github.com/bayugyug/freeformatter  
  
#main entry  
ENTRYPOINT [ "freeformatter" ]  

