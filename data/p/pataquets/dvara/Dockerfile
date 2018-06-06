FROM golang:1  
RUN \  
go get -v github.com/facebookgo/dvara/cmd/dvara  
  
ENTRYPOINT [ "bin/dvara" ]  
CMD [ "--help" ]  

