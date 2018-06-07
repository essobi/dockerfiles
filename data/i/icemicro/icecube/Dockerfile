FROM ubuntu:16.04  
  
ARG BUILD_DATE  
ARG ORG  
ARG SERVICE  
ARG VCS_REF  
ARG VCS_URL  
ARG VENDOR  
ARG VERSION  
  
ENV NAMESPACE="com.${ORG}.${SERVICE}"  
  
LABEL vendor=${VENDOR} \  
${NAMESPACE}.build-date=${BUILD_DATE} \  
${NAMESPACE}.vcs-ref=${VCS_REF} \  
${NAMESPACE}.vcs-url=${VCS_URL} \  
${NAMESPACE}.version=${VERSION}  
RUN apt-get update && apt-get -y upgrade && apt-get install -y \  
iptables \  
libboost-python-dev \  
libffi-dev \  
libnetfilter-queue-dev \  
libssl-dev \  
nfqueue-bindings-python \  
python-pip \  
sudo \  
supervisor \  
tcpdump  
  
RUN pip install --upgrade \  
pip \  
iceman  
  
RUN mkdir -p \  
/etc/${SERVICE} \  
/var/log/supervisor \  
/var/log/${SERVICE}  
RUN echo ${VERSION} > /etc/${SERVICE}/version.txt  
  
ADD bootstrap.sh /bootstrap.sh  
CMD ["bash", "/bootstrap.sh"]  

