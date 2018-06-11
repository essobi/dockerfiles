FROM tyrone98/java8  
MAINTAINER Tyrone "tyrone.dev@gmail.com"  
  
RUN apt-get update \  
&& apt-get install -qy curl zip git bash \  
&& curl -sSL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get update \  
&& apt-get -qy install build-essential nodejs \  
&& npm install -g cnpm gulp \  
&& curl -sSL https://services.gradle.org/distributions/gradle-2.13-bin.zip -o
/tmp/gradle.zip \  
&& unzip /tmp/gradle.zip -d /opt \  
&& ln -s /opt/gradle-2.13/bin/gradle /usr/bin/gradle \  
&& curl -sSL https://get.docker.com/builds/Linux/x86_64/docker-1.11.1.tgz -o
/tmp/docker.tgz \  
&& tar zxf /tmp/docker.tgz -C /tmp \  
&& cp /tmp/docker/docker /usr/bin/docker \  
&& chmod +x /usr/bin/docker \  
&& useradd -u 999 -g root -m jenkins \  
&& mkdir /jenkins \  
&& chown jenkins /jenkins \  
&& curl -sSL http://mirrors.jenkins-ci.org/war/2.0/jenkins.war -o
/opt/jenkins.war \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JENKINS_HOME /jenkins  
  
USER jenkins  
VOLUME /jenkins  
  
EXPOSE 8080  
  
CMD ["java", "-jar", "/opt/jenkins.war"]  
  
  
  

