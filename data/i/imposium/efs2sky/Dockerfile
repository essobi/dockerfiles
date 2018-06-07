FROM golang:1.6-alpine  
  
ADD . /src  
  
RUN mkdir -p src/github.com/NickelMedia && \  
ln -s /src src/github.com/NickelMedia/efs2sky && \  
cd src/github.com/NickelMedia/efs2sky && \  
go install .  
  
ENTRYPOINT ["/go/bin/efs2sky"]  
CMD [""]  

