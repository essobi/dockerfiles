FROM python:2.7.13  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y mysql-server --no-install-recommends \  
&& apt-get clean \  
&& pip install PyMySQL \  
&& pip install MySQL-python \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# This Dockerfile doesn't need to have an entrypoint and a command  
# as Bitbucket Pipelines will overwrite it with a bash script.

