FROM c12e/oracle-jre:8u60b27  
MAINTAINER CognitiveScale.com  
  
ENV JENKINS_HOME=/data \  
JAVA_OPTS="-Xms1024m -Xmx2048m -XX:PermSize=2048m -XX:MaxPermSize=4096m
-Duser.timezone=America/Chicago"  
RUN LAYER=JENKINS \  
&& apk add --update git openssh-client py-pip wget ca-certificates \  
&& apk add --update --repository
http://dl-4.alpinelinux.org/alpine/edge/testing/ tini --allow-untrusted \  
&& pip install ansible-tower-cli \  
&& mkdir -p /jenkins \  
&& wget -P /jenkins http://mirrors.jenkins-ci.org/war/latest/jenkins.war \  
&& apk del wget \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
# for main web interface:  
EXPOSE 8080  
ENTRYPOINT ["tini", "--"]  
ADD run.sh /run.sh  
CMD ["/run.sh"]  

