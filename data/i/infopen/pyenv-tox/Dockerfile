FROM phusion/baseimage:0.10.1  
MAINTAINER Alexandre Chaussier <a.chaussier@infopen.pro>  
  
# Setting for packages installation  
ENV DEBIAN_FRONTEND noninteractive  
  
# Settings about Docker group management  
ARG USER_UID=6000  
ARG USER_NAME=pyenv-test  
  
# Settings about pyenv management  
ENV PYENV_ROOT /home/${USER_NAME}/.pyenv  
ENV PATH ${PYENV_ROOT}/bin:/home/${USER_NAME}/.local/bin:$PATH  
  
# Create user for pyenv  
RUN useradd -m -s /bin/bash -u "${USER_UID}" "${USER_NAME}"  
  
# Manage testing folder  
RUN mkdir -p /srv \  
&& mkdir /srv/app \  
&& mkdir /srv/build \  
&& mkdir /srv/src \  
&& chown -R "${USER_NAME}":"${USER_NAME}" /srv  
WORKDIR /srv/app  
  
# Install openssh, lsb-release and python basics  
RUN apt-get update && \  
apt-get -o Dpkg::Options::="--force-overwrite" install -y \  
curl=7.47.0-1ubuntu2.7 \  
git=1:2.7.4-0ubuntu1.3 \  
libbz2-dev=1.0.6-8 \  
libffi-dev=3.2.1-4 \  
libpython3.5-dev=3.5.2-2ubuntu0~16.04.4 \  
libreadline-dev=6.3-8ubuntu2 \  
libsqlite3-dev=3.11.0-1ubuntu1 \  
libssl-dev=1.0.2g-1ubuntu4.11 \  
libxml2-dev=2.9.3+dfsg1-1ubuntu0.5 \  
libxslt1-dev=1.1.28-2.1ubuntu0.1 \  
locales=2.23-0ubuntu10 \  
lsb-release=9.20160110ubuntu0.2 \  
python3=3.5.1-3 \  
python3-pip=8.1.1-2ubuntu0.4 \  
python3-virtualenv=15.0.1+ds-3ubuntu1 \  
zip=3.0-11  
  
# Locale management  
RUN locale-gen en_US.UTF-8  
RUN echo 'LC_ALL=en_US.UTF-8' > /etc/default/locale  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Tox and Pyenv management  
RUN pip3 install tox==3.0.0 tox-pyenv==1.1.0  
USER ${USER_NAME}  
RUN git clone \--depth 1 --branch v1.1.5 https://github.com/pyenv/pyenv.git
~/.pyenv && \  
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init
-)"\nfi' >> ~/.bashrc && \  
pyenv install 2.7.14 && \  
pyenv install 3.4.7 && \  
pyenv install 3.5.4 && \  
pyenv install 3.6.3  
  
# Default command management  
USER root  
CMD ["/sbin/my_init"]  

