FROM ubuntu:latest  
  
MAINTAINER dianaesteves  
  
ENV OPS_VERSION=2.0.6 \  
OPS=/opt/ops-${OPS_VERSION} \  
PATH=${PATH}:/usr/bin  
  
EXPOSE 8080  
RUN apt-get -y update && apt-get -y install curl && \  
mkdir -p ${OPS} && cd ${OPS} && \  
curl -O --location https://downloads.mongodb.com/on-prem-mms/deb/mongodb-
mms_${OPS_VERSION}.363-1_x86_64.deb && \  
dpkg --install *.deb && \  
rm -rf *.deb  
  
# TODO -- add configs IN PROGRESS -- NOT TESTED  
WORKDIR ${OPS}  
  
ENTRYPOINT ["./opt/${OPS}"]  
CMD ["--help"]  

