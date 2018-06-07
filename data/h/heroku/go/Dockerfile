FROM heroku/go-base:1.4  
RUN mkdir -p /app/.cache/gotools /app/.profile.d  
  
ENV GOPATH /app/.cache/gotools  
ENV PATH $GOPATH/bin:$PATH  
  
RUN go get -u -v github.com/tools/godep  
RUN curl -s --retry 3 -L
https://github.com/stedolan/jq/releases/download/jq-1.4/jq-linux-x86_64 -o
$GOPATH/bin/jq && \  
chmod a+x $GOPATH/bin/jq  
  
ENV GOPATH /app/user  
ENV PATH $GOPATH/bin:$PATH  
  
COPY ./compile /app/.cache/gotools/bin/compile  
  
ONBUILD COPY . /app/.temp  
ONBUILD RUN /app/.cache/gotools/bin/compile  

