FROM moogar0880/glide:latest  
  
LABEL maintainer "moogar0880@gmail.com"  
  
RUN go get -u github.com/derekparker/delve/cmd/dlv  
  
ENTRYPOINT ["/go/bin/dlv"]  
CMD ["--help"]  

