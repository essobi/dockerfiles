FROM golang:alpine  
  
ENV SEARCH_DIR "$GOPATH/src/github.com/schul-cloud/arix-search-adapter/"  
RUN mkdir -p "$SEARCH_DIR"  
ADD . "$SEARCH_DIR"  
RUN go install github.com/schul-cloud/arix-search-adapter  
  
EXPOSE 8080  
ENTRYPOINT ["arix-search-adapter"]  
  

