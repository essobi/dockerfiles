FROM ubuntu:16.04  
  
# Enable source repositories so we can use `apt build-dep` to get all the  
# build dependencies for Python 2.7 and 3.5.  
RUN sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && \  
sed -i -- 's/# deb-src/deb-src/g' /etc/apt/sources.list  
  
# Change these variables to update the version of Python installed.  
ENV PYTHON_34_VER=3.4.7 \  
PYTHON_35_VER=3.5.4 \  
PYTHON_36_VER=3.6.3 \  
PYTHON_27_VER=2.7.13 \  
# Set debian front-end to non-interactive so that apt doesn't ask for  
# prompts later.  
DEBIAN_FRONTEND=noninteractive  
  
ADD get-pythons.sh /usr/local/bin/get-pythons.sh  
# Add a new layer to cache static stuff.  
# Add a new user  
RUN useradd runner \--create-home \  
# Create and change permissions for builds directory  
&& mkdir /builds \  
&& chown runner /builds \  
&& export LC_ALL=C.UTF-8 && export LANG=C.UTF-8  
  
# Add the configuration files to the container.  
COPY mysql.cfg postgres.cfg /home/runner/configs/  
# Change the permissions for configs directory.  
RUN chown -R runner:runner /home/runner/configs \  
# Install the depdencies in the repo.  
&& apt-get -y update && apt-get -y install python-pip python3-pip \  
git openssh-server postgresql-client libpq-dev python3-dev \  
libsqlite3-dev libmysqlclient-dev libreadline-dev libbz2-dev \  
python-dev unzip \  
# Install build dependencies for Python.  
&& apt build-dep -y python2.7 && apt build-dep -y python3.5 \  
&& rm -rf /var/lib/apt/lists/* \  
# Install latest version of tox.  
&& pip3 install tox \  
&& /usr/local/bin/get-pythons.sh  
# Switch to runner user and set the workdir  
USER runner  
WORKDIR /home/runner  

