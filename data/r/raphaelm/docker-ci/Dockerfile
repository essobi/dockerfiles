FROM debian:jessie  
  
MAINTAINER Raphael Michel <mail@raphaelmichel.de>  
# Original copyright by Andrew Munsell  
# https://github.com/andrewmunsell/gitlab-ci-
runner/commit/3c6295fd461d82d3f9a9b6b7fa69a9def5621759  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y locales iptables ca-certificates
lxc \  
apt-transport-https supervisor sudo python3 curl \  
\--no-install-recommends  
RUN echo deb https://apt.dockerproject.org/repo debian-jessie main >
/etc/apt/sources.list.d/docker.list  
RUN echo deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main >
/etc/apt/sources.list.d/ansible.list  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
93C4A3FD7BB9C367  
RUN apt-get update -y && apt-get install -y docker-engine ansible  
  
RUN locale-gen  
RUN update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# We want a current pip  
ADD get-pip.py /tmp/get-pip.py  
RUN python3 /tmp/get-pip.py  
RUN pip install -U virtualenv  
  
ADD wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ADD clean.sh /usr/local/bin/clean.sh  
RUN chmod +x /usr/local/bin/clean.sh  
  
ADD supervisord.conf /etc/supervisor/conf.d/wrapdocker.conf  
  
RUN adduser --disabled-password --gecos '' \--uid 1600 ciuser  
RUN adduser ciuser docker  
RUN echo '\nciuser ALL = (ALL) NOPASSWD:/usr/bin/supervisord' >> /etc/sudoers  
RUN mkdir /builds && chown ciuser /builds  
  
USER ciuser  
  
ENTRYPOINT /usr/local/bin/entrypoint.sh  

