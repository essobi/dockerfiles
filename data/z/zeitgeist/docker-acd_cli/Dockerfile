# vim:set ft=dockerfile:  
# VERSION 1.0  
# AUTHOR: Alexander Turcic <alex@zeitgeist.se>  
# DESCRIPTION: acd_cli in a Docker container  
# TO_BUILD: docker build --rm -t zeitgeist/docker-acdcli .  
# SOURCE: https://github.com/alexzeitgeist/docker-acd_cli  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Alexander Turcic "alex@zeitgeist.se"  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
locales \  
python3-setuptools && \  
easy_install3 -U pip && \  
pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git && \  
apt-get -y purge git && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
sed -i 's/^[^#].*$/# &/' /etc/locale.gen && \  
sed -i 's/^# \\(en_US.UTF-8 UTF-8\\).*$/\1/' /etc/locale.gen && \  
locale-gen && \  
update-locale LANGUAGE=en_US:en LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
RUN \  
export uid=1000 gid=1000 && \  
groupadd --gid ${gid} user && \  
useradd --uid ${uid} \--gid ${gid} \--create-home user  
  
USER user  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/local/bin/acdcli"]  
CMD ["-h"]  

