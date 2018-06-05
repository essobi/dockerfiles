FROM alpine:3.7  
MAINTAINER Viacheslav Kalashnikov <xemuliam@gmail.com>  
  
ARG DIST_MIRROR=http://archive.apache.org/dist/nifi  
ARG VERSION=1.4.0  
ENV NIFI_HOME=/opt/nifi \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk \  
PATH=$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
\  
BANNER_TEXT="" \  
S2S_PORT=""  
RUN apk add --no-cache bash curl openjdk8 && \  
mkdir -p ${NIFI_HOME} && \  
curl ${DIST_MIRROR}/${VERSION}/nifi-${VERSION}-bin.tar.gz | tar xvz -C
${NIFI_HOME} && \  
mv ${NIFI_HOME}/nifi-${VERSION}/* ${NIFI_HOME} && \  
rm -rf ${NIFI_HOME}/nifi-${VERSION} && \  
rm -rf *.tar.gz  
  
ENV CONSUL_TEMPLATE_VERSION=0.19.4  
RUN mkdir -p /tmp/build && \  
cd /tmp/build && \  
curl -O https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
cp consul-template /bin && \  
cd /tmp && \  
rm -rf /tmp/build  
  
VOLUME ${NIFI_HOME}/logs \  
${NIFI_HOME}/flowfile_repository \  
${NIFI_HOME}/database_repository \  
${NIFI_HOME}/content_repository \  
${NIFI_HOME}/provenance_repository \  
/opt/datafiles \  
/opt/scriptfiles \  
/opt/certfiles  
  
WORKDIR ${NIFI_HOME}  
  
EXPOSE 8080 8081 8443  
COPY start_nifi.sh /${NIFI_HOME}/  
RUN mkdir -p /consul-template/template.d/  
ADD template/ /consul-template/template.d/  
  
RUN chmod +x ./start_nifi.sh  
  
CMD ./start_nifi.sh

