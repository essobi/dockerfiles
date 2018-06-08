FROM golang:1.7.3 as xos-cli-builder  
  
ENV WORKDIR /opt/xos-cli  
ENV SOURCEDIR .  
  
COPY ${SOURCEDIR} ${WORKDIR}  
  
WORKDIR ${WORKDIR}  
  
RUN go get github.com/abiosoft/ishell  
RUN go build xos-tosca-cli.go  
  
CMD sleep 86400  

