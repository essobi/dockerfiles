# vim:set ft=dockerfile:  
# VERSION 0.1  
# AUTHOR: Joshua Morris  
# DESCRIPTION: acd_cli in a Docker container  
# TO_BUILD: docker build --rm -t joshuamorris3/docker-cron-acdcli .  
# SOURCE: https://github.com/joshuamorris3/docker-cron-acd_cli  
# Pull base image.  
FROM debian:jessie  
MAINTAINER Joshua Morris  
  
# Install dependencies.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
git \  
locales \  
python3-setuptools \  
wget && \  
easy_install3 -U pip && \  
pip3 install --upgrade git+https://github.com/joshuamorris3/acd_cli.git && \  
apt-get -y purge git && \  
apt-get -y autoremove --purge && \  
rm -rf /var/lib/apt/lists/* && \  
wget -O /usr/local/bin/docker-cron https://github.com/MasteryConnect/docker-
cron/releases/download/v1.3/docker-cron && \  
chmod +x /usr/local/bin/docker-cron  
  
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
  
# Add the 'always sync first' acdcli script  
ADD acdcli_sync /usr/local/bin/  
RUN chmod +x /usr/local/bin/acdcli_sync  
  
USER user  
WORKDIR /tmp  
  
# Run the acdcli_sync job on the schedule defined by the ENV variables passed  
# into this container for docker-cron to run  
ENTRYPOINT ["/usr/local/bin/docker-cron", "/usr/local/bin/acdcli_sync"]  
CMD ["-h"]  

