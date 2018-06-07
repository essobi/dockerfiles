FROM fgrehm/alpine-go:1.5.1  
  
ENV PATH "./node_modules/.bin:$PATH"  
  
USER root  
RUN apk-install nodejs \  
&& go get -u github.com/jteeuwen/go-bindata/... \  
&& go get github.com/elazarl/go-bindata-assetfs/... \  
&& chown 1000:1000 -R $GOPATH \  
&& chown 1000:1000 -R $GOROOT  
USER developer  

