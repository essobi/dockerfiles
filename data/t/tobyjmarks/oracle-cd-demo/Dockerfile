#  
# Inherit from the latest Jenkins 2.0 build (because we want pipeline
functionality)  
#  
FROM jenkinsci/jenkins  
  
#  
# It's-a-me  
#  
MAINTAINER tobyjmarks@gmail.com  
  
#  
# Pre-install selected Jenkins plugins and disable banner page  
#  
USER jenkins  
COPY plugins.txt /usr/share/jenkins/ref/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt \  
&& echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
  
#  
# We need to install Docker and other necessary apps as root  
#  
USER root  
  
#  
# Install Docker prereqs, including supervisor to start the daemon  
#  
RUN apt-get update -qq && apt-get install -qqy apt-transport-https ca-
certificates supervisor  
  
#  
# Create log folders for supervisor, jenkins and docker  
#  
RUN mkdir -p /var/log/supervisor \  
&& mkdir -p /var/log/docker \  
&& mkdir -p /var/log/jenkins  
  
#  
# Allow jenkins to write logs to /var/log  
#  
RUN chown root:jenkins /var/log \  
&& chmod 775 /var/log \  
&& chown root:jenkins /var/log/jenkins \  
&& chmod 775 /var/log/jenkins  
  
#  
# Install Docker  
#  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >>
/etc/apt/sources.list.d/docker.list \  
&& apt-get update -qq \  
&& apt-get install -qqy docker-engine  
  
#  
# Add jenkins to docker group so jenkins has permission to run docker  
#  
#RUN groupadd docker # not needed; already exists  
RUN gpasswd -a jenkins docker  
RUN gpasswd -a jenkins staff # when mapping /var/run/docker.sock from host  
  
#  
# Install the magic wrapper  
#  
COPY ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
#  
# Install the supervisor config file  
#  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#  
# Start Jenkins, Docker  
#  
ENTRYPOINT ["/usr/bin/supervisord", "-c",
"/etc/supervisor/conf.d/supervisord.conf"]  

