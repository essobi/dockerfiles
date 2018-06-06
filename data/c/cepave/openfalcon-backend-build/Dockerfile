FROM golang:1.7  
  
MAINTAINER minimum@cepave.com  
  
ARG ENTRYFILE=openfalcon-build.sh  
ARG BRANCH  
ENV BRANCH=${BRANCH:-develop} REPO=github.com/Cepave/open-falcon-backend  
ENV WORKPATH=${GOPATH}/src/${REPO}  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/go/bin:$GOPATH/bin  
  
# Build Open-Falcon Components  
VOLUME /package  
  
RUN \  
apt-get update \  
&& apt-get install -y git g++ make \  
&& mkdir -p ${WORKPATH}  
  
COPY ${ENTRYFILE} build.sh  
  
# Start  
ENTRYPOINT ["/bin/bash"]  
CMD ["build.sh"]  

