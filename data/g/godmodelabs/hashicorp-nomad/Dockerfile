# Using debian because busybox:glibc does not include libpthread.so  
FROM debian:latest  
MAINTAINER it-operations@boerse-go.de  
ENV TOOL=nomad \  
VERSION=0.3.2 \  
SHA256=710ff3515bc449bc2a06652464f4af55f1b76f63c77a9048bc30d6fde284b441  
  
# By using ADD there is no need to install wget or curl  
ADD
https://releases.hashicorp.com/${TOOL}/${VERSION}/${TOOL}_${VERSION}_linux_amd64.zip
${TOOL}_${VERSION}_linux_amd64.zip  
RUN echo "${SHA256} ${TOOL}_${VERSION}_linux_amd64.zip" | sha256sum -cw &&\  
apt-get update -y &&\  
apt-get install -y unzip &&\  
unzip ${TOOL}_${VERSION}_linux_amd64.zip &&\  
rm -r ${TOOL}_${VERSION}_linux_amd64.zip &&\  
apt-get clean && rm -r /var/lib/apt/lists/*  
  
EXPOSE :4646 :4647 :4648  
ENTRYPOINT ["/nomad"]  
CMD ["--help"]  

