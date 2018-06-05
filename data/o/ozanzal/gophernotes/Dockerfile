FROM jupyter/notebook  
  
# dependencies  
RUN apt-get update  
RUN apt-get install -y pkg-config libzmq-dev build-essential curl bzip2 tar
ca-certificates  
  
# set up golang  
RUN curl -L https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz >
golang.tar.gz && \  
tar -C /usr/local -xzf golang.tar.gz  
ENV PATH /usr/local/go/bin:$PATH  
ENV GOPATH /go  
ENV PATH $GOROOT/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
# install gophernotes  
RUN go get golang.org/x/tools/cmd/goimports  
RUN go get github.com/gophergala2016/gophernotes  
RUN mkdir -p ~/.ipython/kernels/gophernotes  
RUN cp -r $GOPATH/src/github.com/gophergala2016/gophernotes/kernel/*
~/.ipython/kernels/gophernotes  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook"]  

