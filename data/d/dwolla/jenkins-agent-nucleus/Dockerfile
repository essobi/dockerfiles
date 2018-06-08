FROM alpine:latest AS builder  
ENV JENKINS_HOME=/home/jenkins \  
JENKINS_AGENT=/usr/share/jenkins \  
AGENT_VERSION=2.62.6  
COPY jenkins-agent /usr/local/bin/jenkins-agent  
COPY README-extension.md /opt/image-extension/README.md  
  
RUN apk add --update \  
ca-certificates \  
curl \  
&& \  
curl --create-dirs -sSLo ${JENKINS_AGENT}/agent.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar && \  
chmod 755 ${JENKINS_AGENT} && \  
chmod 644 ${JENKINS_AGENT}/agent.jar && \  
chmod 755 /opt/image-extension && \  
chmod 644 /opt/image-extension/*  
  
FROM scratch  
  
COPY \--from=builder /usr/local/bin /usr/local/bin  
COPY \--from=builder /usr/share/jenkins /usr/share/jenkins  
COPY \--from=builder /opt/image-extension /opt/image-extension  

