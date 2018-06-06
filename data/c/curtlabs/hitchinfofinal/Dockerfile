FROM golang:1.4  
RUN mkdir -p /home/deployer/gosrc/src/github.com/curt-labs/HitchInfoFinal  
ADD . /home/deployer/gosrc/src/github.com/curt-labs/HitchInfoFinal  
WORKDIR /home/deployer/gosrc/src/github.com/curt-labs/HitchInfoFinal  
RUN export GOPATH=/home/deployer/gosrc && go get  
RUN export GOPATH=/home/deployer/gosrc && go build -o HitchInfoFinal
./index.go  
  
ENTRYPOINT /home/deployer/gosrc/src/github.com/curt-
labs/HitchInfoFinal/HitchInfoFinal  
  
EXPOSE 8080  

