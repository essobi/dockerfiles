FROM debian:stretch  
MAINTAINER Leandro Lisboa Penz <lpenz@lpenz.org>  
  
# install debian packages:  
ENV DEBIAN_FRONTEND=noninteractive  
RUN set -x -e; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# shell:  
shellcheck \  
# yaml:  
python3-yaml \  
# python:  
flake8 \  
# omnilint:  
python-setuptools python-pip python-wheel python3-lxml \  
# base packages:  
locales gosu sudo  
  
# setup sudo and locale  
RUN set -x -e; \  
echo 'ALL ALL=NOPASSWD:ALL' > /etc/sudoers.d/all; \  
chmod 0400 /etc/sudoers.d/all; \  
mkdir /target; \  
echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen; \  
locale-gen  
ENV LC_ALL=en_US.UTF-8  
# install pip packages:  
RUN set -x -e; \  
pip install \  
py3kwarn==0.4.4  
  
COPY container/omnilint-analyse /usr/local/bin/omnilint-analyse  
COPY container/omnilint /usr/local/lib/python3.5/dist-packages/omnilint  
  
# setup entrypoint with user UID/GID from host  
RUN set -x -e; \  
(\  
echo '#!/bin/bash'; \  
echo 'MY_UID=${MY_UID:-1000}'; \  
echo 'set -e'; \  
echo 'useradd -M -u "$MY_UID" -o user'; \  
echo 'cd $RWD'; \  
echo 'exec gosu user "${@:-/bin/bash}"'; \  
) > /usr/local/bin/entrypoint.sh; \  
chmod a+x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["/usr/local/bin/omnilint-analyse","."]  
  
# Run the container as:  
# docker run -it --rm -v $PWD:$PWD -e RWD=$PWD -e MY_UID=$UID omnilint  

