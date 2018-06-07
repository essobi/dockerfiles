FROM debian:stretch  
  
MAINTAINER Stephane Cottin <stephane.cottin@vixns.com>  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
python-setuptools \  
apt-transport-https \  
ca-certificates \  
curl \  
git \  
lxc \  
iptables  
  
# Install syslog-stdout  
RUN easy_install syslog-stdout supervisor-stdout  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install Docker Compose  
ENV DOCKER_COMPOSE_VERSION 1.12.0  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
# Install the wrapper script from
https://raw.githubusercontent.com/docker/docker/master/hack/dind.  
ADD ./dind /usr/local/bin/dind  
RUN chmod +x /usr/local/bin/dind  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Install Jenkins  
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -  
RUN sh -c 'echo deb https://pkg.jenkins.io/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN apt-get update && apt-get install -y openjdk-8-jdk-headless zip supervisor
jenkins && rm -rf /var/lib/apt/lists/*  
RUN usermod -a -G docker jenkins  
ENV JENKINS_HOME /var/lib/jenkins  
VOLUME /var/lib/jenkins  
  
# get plugins.sh tool from official Jenkins repo  
# this allows plugin installation  
ENV JENKINS_UC https://updates.jenkins.io  
  
RUN curl -o /usr/local/bin/plugins.sh \  
https://raw.githubusercontent.com/jenkinsci/docker/75b17c48494d4987aa5c2ce7ad02820fda932ce4/plugins.sh
&& \  
chmod +x /usr/local/bin/plugins.sh  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# install python tools  
RUN easy_install pip  
  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
# copy files onto the filesystem  
COPY files/ /  
RUN chmod +x /docker-entrypoint /usr/local/bin/*  
  
EXPOSE 8080  
# set the entrypoint  
ENTRYPOINT ["/docker-entrypoint"]  
  
CMD ["/usr/bin/supervisord"]  

