FROM muicoder/glibc:golang AS build  
  
ARG WORK=/build  
WORKDIR $WORK  
  
SHELL ["bash", "-c"]  
# wide  
RUN go get github.com/b3log/wide \  
github.com/bradfitz/goimports \  
github.com/visualfc/gotools \  
github.com/nsf/gocode && \  
mv -fv $GOPATH/src/github.com/b3log/wide/{conf,i18n,static,views} $WORK && \  
mv -fv $GOPATH/bin/{wide,gocode,goimports,gotools} $WORK && \  
rm -rf $GOPATH/{src,bin,pkg}/* $WORK/{conf,i18n}/*.go  
  
FROM muicoder/glibc  
  
ARG WORK=/usr/local/bin  
WORKDIR $WORK  
  
COPY \--from=build /build/* $WORK/  
COPY wide .  
  
CMD ["wide", "--help"]  

