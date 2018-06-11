FROM nginx  
  
MAINTAINER Veekee  
  
ENV GO_VERSION 1.8  
ENV INSTALL_BASE=/root  
ENV GOROOT=${INSTALL_BASE}/go  
ENV GOPATH=${INSTALL_BASE}/nginx_exporter  
  
RUN apt-get clean && \  
apt-get -q -y update && \  
apt-get -q -y install \  
wget \  
git  
  
RUN cd ${INSTALL_BASE} && wget -O ${INSTALL_BASE}/go.tar.gz
https://storage.googleapis.com/golang/go${GO_VERSION}.linux-amd64.tar.gz  
RUN cd ${INSTALL_BASE} && tar -xvf ${INSTALL_BASE}/go.tar.gz && rm -f
${INSTALL_BASE}/go.tar.gz  
RUN ls -l ${INSTALL_BASE}  
RUN cd ${INSTALL_BASE} && git clone
https://github.com/discordianfish/nginx_exporter  
RUN cd ${GOPATH} && ${GOROOT}/bin/go get
"github.com/prometheus/client_golang/prometheus"  
RUN cd ${GOPATH} && ${GOROOT}/bin/go get "github.com/prometheus/log"  
RUN cd ${GOPATH} && ${GOROOT}/bin/go build  
RUN rm -rf ${GOROOT}  
  
COPY startPrometheusExporter.sh ${GOPATH}/startPrometheusExporter.sh  
COPY startDeamon.sh ${GOPATH}/startDeamon.sh  
  
RUN chmod +x ${GOPATH}/*.sh  
  
EXPOSE 9113  
CMD ${GOPATH}/startDeamon.sh  

