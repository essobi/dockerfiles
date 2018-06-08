FROM ubuntu:xenial  
MAINTAINER Stephane Jourdan <sjourdan@greenalto.com>  
ENV REFRESHED_AT 2016-09-07  
ENV NOMAD_VERSION 0.4.1  
ENV NOMAD_ARCHIVE=nomad.zip  
  
RUN apt-get update -yqq && \  
apt-get install -yqq ca-certificates curl unzip && \  
apt-get clean && \  
# rm -rf /var/lib/apt/lists/* \  
curl -o ${NOMAD_ARCHIVE}
"https://releases.hashicorp.com/nomad/${NOMAD_VERSION}/nomad_${NOMAD_VERSION}_linux_amd64.zip"
&&\  
unzip ${NOMAD_ARCHIVE} -d /bin && \  
chmod +x /bin/nomad && \  
rm -rf ${NOMAD_ARCHIVE} && \  
apt-get remove -y curl unzip  
  
ENTRYPOINT ["/bin/nomad"]  
CMD ["--help"]  

