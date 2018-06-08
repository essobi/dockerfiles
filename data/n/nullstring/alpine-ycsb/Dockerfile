FROM alpine:latest  
  
MAINTAINER dianaesteves  
  
ENV YCSB_VERSION=0.10.0 \  
YCSB=/opt/ycsb-${YCSB_VERSION} \  
PATH=${PATH}:/usr/bin  
  
# exposed port -- spells YCSB in a dial pad :)  
EXPOSE 9272  
RUN apk update && apk add --update curl python openjdk7-jre && \  
mkdir /opt && cd /opt && \  
curl -O --location
https://github.com/brianfrankcooper/YCSB/releases/download/${YCSB_VERSION}/ycsb-${YCSB_VERSION}.tar.gz
&& \  
tar xfz *.tar.gz && \  
rm -rf *.tar.gz  
  
WORKDIR ${YCSB}  
  
ENTRYPOINT ["./bin/ycsb"]  
CMD ["--help"]  
  

