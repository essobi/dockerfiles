# Build using: docker build -f Dockerfile.gocd-agent -t gocd-agent .  
FROM c12e/dind:1.11.2-alpine36  
  
# version is a mess as the zip doesn't include the build number..  
RUN apk --no-cache add python py-pip bash unzip openjdk8-jre git curl openssh
jq ca-certificates \  
&& CONSUL_TEMPLATE_VERSION=0.14.0 \  
&& wget https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& mv consul-template /usr/local/bin/consul-template \  
&& rm consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& mkdir -p /consul-template /consul-template/config.d /consul-
template/templates \  
&& AGNT_VER=17.5.0-5095 \  
&& FOLDER_NAME=go-agent-$(echo $AGNT_VER | cut -d'-' -f1) \  
&& curl https://download.gocd.org/binaries/${AGNT_VER}/generic/go-
agent-${AGNT_VER}.zip -o /tmp/go-agent.zip \  
&& mkdir -p /opt \  
&& cd /opt \  
&& unzip /tmp/go-agent.zip \  
&& chmod +x /opt/${FOLDER_NAME}/agent.sh \  
&& pip install docker-compose awscli \  
&& ln -s /opt/${FOLDER_NAME} /opt/go-agent \  
&& rm -r /tmp/* \  
&& mkdir -p /root/.config/git \  
&& echo "cruise-output/" >> /root/.config/git/ignore  
  
ADD deploy/run.sh /run.sh  
ADD bin/ /usr/local/bin/  
ADD etc/ /usr/local/etc/  
ENV JAVA_HOME=/usr GO_SERVER=go-server GO_SERVER_PORT=8153  
WORKDIR /tmp  
VOLUME ["/work","/root"]  
STOPSIGNAL HUP  
  
CMD ["/run.sh"]  

