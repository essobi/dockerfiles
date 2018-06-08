# Open Monitoring Distribution  
#  
# Forked from https://github.com/fstab/docker-omd  
#  
## Version: 1.0  
FROM ubuntu:16.04  
MAINTAINER Steffen Schüssler, software@neffets.de  
  
# Var for first config  
ENV DEBIAN_FRONTEND="noninteractive" \  
SITENAME="monitor" \  
OMD_APACHE_TCP_ADDR="0.0.0.0" \  
OMD_APACHE_TCP_PORT="5000" \  
OMD_TMPFS="off"  
RUN mkdir -p /opt/omd && ln -sf /opt/omd /omd  
  
# Install OMD, see http://labs.consol.de/OMD/  
RUN gpg --keyserver keys.gnupg.net --recv-keys F8C1CA08A57B9ED7 \  
&& gpg --armor --export F8C1CA08A57B9ED7 | apt-key add \- \  
&& echo "deb http://labs.consol.de/repo/stable/ubuntu xenial main" >>
/etc/apt/sources.list  
  
# Make sure package repository is up to date  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y libpython2.7 \  
python3-setuptools python3-setuptools-git python3-wheel python3-pip \  
net-tools netcat wget iputils-ping \  
postfix mutt  
  
RUN apt-get install -y omd \  
check-mk-agent  
#RUN pip3 install check_docker \  
# && apt-get clean all  
# Fix some stuff in apache: no change ulimit and give the server a name  
RUN echo "APACHE_ULIMIT_MAX_FILES=true" >> /etc/apache2/envvars \  
&& echo ServerName docker-omd > /etc/apache2/conf-available/docker-
servername.conf \  
&& a2enconf docker-servername  
  
VOLUME /opt/omd/sites  
  
# Add watchdog script  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod a+rx /usr/local/bin/entrypoint.sh  
  
# Set up runtime options  
EXPOSE 5000  
ENTRYPOINT ["entrypoint.sh"]  

