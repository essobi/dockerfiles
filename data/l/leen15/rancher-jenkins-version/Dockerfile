FROM ubuntu:16.04  
MAINTAINER Luca Mattivi <luca@smartdomotik.com>  
  
# expose the port  
EXPOSE 8080  
# required to make docker in docker to work  
VOLUME /var/lib/docker  
  
# default jenkins home directory  
ENV JENKINS_HOME /var/jenkins  
# set our user home to the same location  
ENV HOME /var/jenkins  
  
# set our wrapper  
ENTRYPOINT ["/usr/local/bin/docker-wrapper"]  
# default command to launch jenkins  
CMD java -jar /usr/share/jenkins/jenkins.war  
  
# setup our local files first  
ADD docker-wrapper.sh /usr/local/bin/docker-wrapper  
  
# for installing docker related files first  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >
/etc/apt/sources.list.d/universe.list  
# apparmor is required to run docker server within docker container  
RUN apt-get update -qq && apt-get install -qqy wget curl git iptables ca-
certificates apparmor  
  
# now we install docker in docker - thanks to https://github.com/jpetazzo/dind  
# We install newest docker into our docker in docker container  
#ADD https://get.docker.io/builds/Linux/x86_64/docker-latest
/usr/local/bin/docker  
#RUN chmod +x /usr/local/bin/docker  
RUN curl -L https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz >
/tmp/docker-latest.tgz && \  
cd /tmp && tar -xzf ./docker-latest.tgz && \  
rm /tmp/docker-latest.tgz && \  
mv /tmp/docker/docker /usr/local/bin/docker && \  
chmod +x /usr/local/bin/docker  
  
# for jenkins  
RUN echo deb http://pkg.jenkins-ci.org/debian-stable/ binary/ >>
/etc/apt/sources.list \  
&& wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN apt-get update -qq && apt-get install -qqy jenkins  

