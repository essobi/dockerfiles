FROM node:6.7  
RUN apt-get update \  
&& apt-get install -y postgresql postgresql-contrib \  
&& apt-get install sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# This Dockerfile doesn't need to have an entrypoint and a command  
# as Bitbucket Pipelines will overwrite it with a bash script.

