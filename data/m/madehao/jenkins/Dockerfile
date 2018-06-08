FROM madehao/jdk:8-centos7  
  
MAINTAINER madehao1983@sina.com  
  
# install python  
WORKDIR /tmp  
  
RUN yum -y install gcc make zlib-devel openssl-devel \  
&& curl -o Python-2.7.14.tgz \  
https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz \  
&& tar -zxvf Python-2.7.14.tgz \  
&& rm -f Python-2.7.14.tgz  
  
WORKDIR /tmp/Python-2.7.14  
  
RUN ./configure --enable-optimizations \  
&& make \  
&& make install  
  
WORKDIR /  
  
RUN mv /usr/bin/python2.7 /usr/bin/python2.7.5 \  
&& mv /usr/bin/pydoc /usr/bin/pydoc2.7.5 \  
&& ln -s /usr/local/bin/python /usr/bin/python2.7 \  
&& ln -s /usr/local/bin/pydoc /usr/bin/pydoc \  
&& ln -s /usr/local/bin/python-config /usr/bin/python-config \  
&& curl https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install requests \  
&& sed -i 's;/usr/bin/python;/usr/bin/python2.7.5;' /usr/bin/yum \  
&& sed -i 's;/usr/bin/python;/usr/bin/python2.7.5;' /usr/bin/urlgrabber \  
&& sed -i 's;/usr/bin/python;/usr/bin/python2.7.5;' /usr/libexec/urlgrabber-
ext-down \  
&& sed -i 's;/usr/bin/python;/usr/bin/python2.7.5;' /usr/bin/yum-config-
manager \  
&& rm -fr /tmp/Python-2.7.14  
  
# install git nodejs maven sonar-scanne rancher which(maven need)  
COPY rancher /usr/local/bin/rancher  
  
RUN yum-config-manager \  
\--add-repo \  
https://download.docker.com/linux/centos/docker-ce.repo \  
&& yum install -y git subversio docker-ce which \  
&& curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - \  
&& yum -y install nodejs \  
&& chmod 755 /usr/local/bin/rancher  
  
WORKDIR /tmp  
  
RUN curl -o apache-maven-3.3.9-bin.tar.gz \  
https://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz \  
&& tar -zxvf apache-maven-3.3.9-bin.tar.gz \  
&& mv apache-maven-3.3.9 /usr/local/ \  
&& ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/local/bin/mvn \  
&& rm -f apache-maven-3.3.9-bin.tar.gz \  
&& curl -o sonar-scanner-cli-3.0.3.778-linux.zip \  
-L https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778-linux.zip \  
&& jar -xvf sonar-scanner-cli-3.0.3.778-linux.zip \  
&& mv sonar-scanner-3.0.3.778-linux /usr/local/ \  
&& chmod 755 /usr/local/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner \  
/usr/local/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner-debug \  
/usr/local/sonar-scanner-3.0.3.778-linux/jre/bin/java \  
&& ln -s /usr/local/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner
/usr/local/bin/sonar-scanner \  
&& rm -f sonar-scanner-cli-3.0.3.778-linux.zip  
  
# install jenkins  
WORKDIR /  
  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ARG http_port=8080  
ARG agent_port=50000  
ENV JENKINS_HOME /var/jenkins_home  
ENV JENKINS_SLAVE_AGENT_PORT ${agent_port}  
ENV LANG "zh_CN.UTF-8"  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d /home/${user} -u ${uid} -g ${gid} -G docker -m -s /bin/bash
${user} \  
&& mkdir /usr/share/jenkins /home/${user}/.m2 /var/jenkins_home \  
&& chown jenkins:jenkins /var/jenkins_home  
  
COPY agent.jar /usr/share/jenkins/agent.jar  
COPY settings.xml /home/${user}/.m2/settings.xml  
  
RUN curl -o /usr/share/jenkins/jenkins.war \  
-L http://mirrors.jenkins.io/war-stable/latest/jenkins.war \  
&& chown -R ${user}:${group} /home/${user}/.m2  
  
VOLUME ["/var/jenkins_home"]  
  
EXPOSE 8080 50000  
USER jenkins  
CMD
["java","-server","-Xms4g","-Xmx4g","-XX:+UseG1GC","-Djava.security.egd=file:/dev/urandom","-jar","/usr/share/jenkins/jenkins.war"]  

