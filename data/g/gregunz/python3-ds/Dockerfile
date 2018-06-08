# PYTHON3-DOCKER  
#  
# DEPENDENCIES (to reuse this Dockerfile):  
# - apt-packages.txt at /requirements  
# - python-pre-packages.txt at /requirements  
# - python-packages.txt at /requirements  
# - start_docker.sh at /scripts  
FROM debian:stretch  
  
LABEL maintainer="gregunz <contact@gregunz.io>"  
  
# Export env settings  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm \  
LANG=en_US.UTF-8 \  
PYTHON_HOME=/usr/bin/python3 \  
PYTHON_ENV_HOME=/opt/ds \  
SHELL_HOME=/bin/bash  
  
ADD /requirements /tmp/requirements  
ADD /scripts /tmp/scripts  
  
# MAKE SCRIPTS EXECUTABLE  
RUN set -x \  
&& chmod +x tmp/scripts/*  
  
# INSTALL REQUIREMENTS  
RUN set -x \  
&& apt-get update -y \  
&& xargs -a /tmp/requirements/apt-packages.txt apt-get install -y \  
&& pip install virtualenv \  
&& /usr/local/bin/virtualenv $PYTHON_ENV_HOME \--distribute
--python=$PYTHON_HOME \  
&& $PYTHON_ENV_HOME/bin/pip install -r /tmp/requirements/python-pre-
packages.txt \  
&& $PYTHON_ENV_HOME/bin/pip install -r /tmp/requirements/python-packages.txt  
  
# REMOVING REQUIREMENTS DIR  
RUN set -x \  
&& rm -rf /tmp/requirements  
  
WORKDIR $PYTHON_ENV_HOME  
EXPOSE 8888  
ENTRYPOINT ["/tmp/scripts/start_docker.sh"]  

