# GolangFileServer  
#  
# VERSION 1.0  
FROM oceanwu/godepffmpeg:latest  
  
MAINTAINER oceanwu<wuhaiyang1213@gmail.com>  
  
# build & run golangfieserver  
ENV kpdir /go/src/golang-pipVideo-mixAudio  
  
RUN mkdir -p ${kpdir}  
  
ADD . ${kpdir}/  
  
WORKDIR ${kpdir}  
  
RUN go build -v  
  
EXPOSE 8089  
ENTRYPOINT ["./golang-pipVideo-mixAudio"]  
  

