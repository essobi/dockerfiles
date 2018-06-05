FROM openjdk:8  
MAINTAINER Martin Ponbauer <martin.ponbauer@hotmail.com>  
  
#This makes debconf use a frontend that expects no interactive input at all  
ARG DEBIAN_FRONTEND=noninteractive  
  
#Default environment variables that can be used to modify the installation  
ENV BAMBOO_HOME /var/atlassian/bamboo  
ENV BAMBOO_INSTALL /opt/atlassian/bamboo  
ENV BAMBOO_VERSION 6.3.3  
ENV NODE_JS_VERSION 8.x  
ENV MYSQL_CONNECTOR_JAVA_VERSION 5.1.46  
ENV DOCKER_VERSION 18.03.0~ce-0~debian  
  
#Download and Install required packages to proceed  
RUN apt-get update && \  
apt-get -y install --no-install-recommends apt-utils && \  
apt-get -y install curl wget && \  
apt-get -y install vim nano && \  
apt-get -y install openssl && \  
apt-get -y install bzip2 xz-utils unzip locales  
  
#Download and Install Bamboo (including MySQL Java Connector)  
RUN mkdir -p ${BAMBOO_INSTALL} ${BAMBOO_HOME} && \  
wget https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-${BAMBOO_VERSION}.tar.gz -q && \  
tar -xvf atlassian-bamboo-${BAMBOO_VERSION}.tar.gz && \  
rm -f atlassian-bamboo-${BAMBOO_VERSION}.tar.gz && \  
mv atlassian-bamboo-${BAMBOO_VERSION}/* ${BAMBOO_INSTALL} && \  
echo "bamboo.home=${BAMBOO_HOME}" >> ${BAMBOO_INSTALL}/atlassian-bamboo/WEB-
INF/classes/bamboo-init.properties && \  
curl -Ls "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_JAVA_VERSION}.tar.gz" | tar -xz --directory
"${BAMBOO_INSTALL}/lib" \--strip-components=1 --no-same-owner "mysql-
connector-java-${MYSQL_CONNECTOR_JAVA_VERSION}/mysql-connector-
java-${MYSQL_CONNECTOR_JAVA_VERSION}-bin.jar"  
  
#Download and Install Docker inside the container  
RUN apt-get update && \  
apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-
properties-common && \  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(.
/etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \  
apt-get update && \  
apt-get -y install docker-ce=${DOCKER_VERSION}  
  
#Download and Install Nodes.js and webdriver-manager  
RUN curl -sL https://deb.nodesource.com/setup_${NODE_JS_VERSION} | bash - && \  
apt-get update && \  
apt-get -y install python2.7 && \  
apt-get install -y nodejs && \  
apt-get install -y build-essential && \  
npm install -g --unsafe-perm webdriver-manager  
  
#Download and Install Chrome (e.g. for automated UI testing frameworks)  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' && \  
apt-get update && apt-get install -y google-chrome-stable  
  
#Change directory to the Bamboo installation directory  
WORKDIR $BAMBOO_HOME  
  
EXPOSE 8085 8443  
#Start Bamboo in the foreground  
CMD ["/opt/atlassian/bamboo/bin/start-bamboo.sh", "-fg"]  

