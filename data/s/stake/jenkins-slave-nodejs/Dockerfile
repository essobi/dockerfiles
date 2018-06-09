FROM openshift/jenkins-slave-base-centos7  
  
USER root  
  
ENV NODEJS_VERSION=8 \  
NPM_CONFIG_PREFIX=$HOME/.npm-global \  
PATH=$HOME/node_modules/.bin/:$HOME/.npm-global/bin/:$PATH  
  
# Install NodeJS  
RUN curl -sL https://rpm.nodesource.com/setup_8.x | bash - && \  
yum install -y --setopt=tsflags=nodocs nodejs bzip2 fontconfig  
  
# Install Build Tools  
RUN yum install -y gcc-c++ make python  
  
RUN npm install -g gulp-cli  
  
# Install Google Chrome  
ADD ./google-x86_64.repo /etc/yum.repos.d/external.repo  
RUN yum install -y google-chrome-stable gnu-free-sans-fonts  
  
# Install Groovy  
RUN cd /opt && \  
curl -L -o groovy-all-2.4.13.jar
http://central.maven.org/maven2/org/codehaus/groovy/groovy-all/2.4.13/groovy-
all-2.4.13.jar  
ENV GROOVY_JAR=/opt/groovy-all-2.4.13.jar  
  
# Install OWASP ZAP  
ENV ZAP_PATH=/opt/ZAP  
RUN cd /opt && \  
curl -L -o ZAP.tar.gz
https://github.com/zaproxy/zaproxy/releases/download/2.6.0/ZAP_2.6.0_Linux.tar.gz
&& \  
mkdir temp && \  
tar zxvf ZAP.tar.gz -C ./temp && \  
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
  
# Install OWASP Dependency-Check  
ARG DEPENDENCY_CHECK_DOWNLOAD_URL  
RUN cd /opt && \  
curl -L -o dependency-check.tar.gz https://bintray.com/jeremy-
long/owasp/download_file?file_path=dependency-check-3.1.0-release.zip && \  
mkdir temp && \  
unzip dependency-check.tar.gz -d ./temp && \  
DEPENDENCY_CHECK_DIR_NAME=$(ls -1 ./temp) && \  
mv ./temp/${DEPENDENCY_CHECK_DIR_NAME} dependency-check && \  
rm -rf temp && \  
chown 1001:0 -R dependency-check && \  
chmod a+w -R dependency-check  
  
# Install Mono  
RUN yum install -y mono-core mono-devel  
  
RUN yum clean all  
  
RUN chown -R 1001:0 $HOME && \  
chmod -R g+rwx $HOME  
  
USER 1001  

