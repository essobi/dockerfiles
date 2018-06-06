FROM golang:1.7.1  
RUN mkdir -p "$GOPATH/src/github.com/kuberlab/helm-deployer"  
  
COPY . "$GOPATH/src/github.com/kuberlab/helm-deployer"  
  
RUN go install -v "github.com/kuberlab/helm-deployer"  
  
CMD [ "helm-deployer" ]  
  
EXPOSE 12122  

