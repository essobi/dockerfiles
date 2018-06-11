FROM gliderlabs/alpine:3.3  
MAINTAINER Maurice carey <maurice@mauricecarey.com>  
  
ENV CONSUL_TEMPLATE_VERSION 0.14.0  
ENV CONSUL_TEMPLATE_TMP /tmp/consul-template.zip  
ENV CONSUL_TEMPLATE_HOME /usr/local/bin  
  
RUN apk --no-cache add \  
ca-certificates \  
wget &&\  
wget --quiet --output-document=${CONSUL_TEMPLATE_TMP}
https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip &&\  
unzip ${CONSUL_TEMPLATE_TMP} -d ${CONSUL_TEMPLATE_HOME} &&\  
rm -f ${CONSUL_TEMPLATE_TMP} &&\  
mkdir -p /consul-template/{config.d,templates}  
  
ENTRYPOINT ["/usr/local/bin/consul-template"]  

