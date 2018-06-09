FROM openshift/jenkins-slave-maven-centos7  
  
USER root  
  
# Install Groovy  
RUN cd /opt && \  
curl -L -o groovy-all-2.4.13.jar
http://central.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.13/groovy-
all-2.4.13.jar  
ENV GROOVY_JAR=/opt/groovy-all-2.4.13.jar  
  
# Install OWASP ZAP  
ARG ZAP_DOWNLOAD_URL  
ENV ZAP_PATH=/opt/ZAP  
RUN cd /opt && \  
curl -L -o ZAP.tar.gz
https://github.com/zaproxy/zaproxy/releases/download/2.6.0/ZAP_2.6.0_Linux.tar.gz
&& \  
mkdir temp && \  
tar zxf ZAP.tar.gz -C ./temp && \  
ZAP_DIR_NAME=$(ls -1 ./temp) && \  
mv ./temp/${ZAP_DIR_NAME} ZAP && \  
rm -rf temp && \  
rm ZAP.tar.gz && \  
chown 1001:0 -R ZAP && \  
chmod a+w -R ZAP && \  
mkdir -p /home/jenkins/.ZAP  
ADD .ZAP_JVM.properties /home/jenkins/.ZAP/  
RUN yum install -y wget && \  
yum install -y epel-release && \  
yum install -y python-pip && \  
pip install --upgrade zapcli  
  
# Install Mono  
RUN yum install -y mono-core mono-devel  
  
RUN yum clean all  
  
RUN chown -R 1001:0 $HOME && \  
chmod -R g+rw $HOME  
  
USER 1001  

