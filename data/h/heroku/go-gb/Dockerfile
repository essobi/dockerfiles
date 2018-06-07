FROM heroku/go-base:1.4  
RUN mkdir -p /app/.cache/gotools /app/.profile.d  
  
ENV GOPATH /app/.cache/gotools  
ENV PATH /app/user/bin:$GOPATH/bin:$PATH  
ENV GBVERSION 0.4.0  
RUN mkdir -p $GOPATH/src/github.com/constabulary && \  
cd $GOPATH/src/github.com/constabulary && \  
curl -s "https://codeload.github.com/constabulary/gb/tar.gz/v$GBVERSION" | tar
zxf - && \  
mv gb-$GBVERSION gb && \  
cd gb && \  
go install -v ./... && \  
cd $GOPATH && \  
rm -rf src pkg  
  
COPY ./go-gb-docker.sh /app/.profile.d/go-gb-docker.sh  
  
ONBUILD COPY . /app/user  
ONBUILD RUN gb info && \  
gb build  

