FROM selenium/node-firefox:3.12.0-americium  
MAINTAINER Global Solutions co., ltd.  
  
USER root  
RUN apt-get update -qqy && apt-get install --no-install-recommends -y fonts-
ipafont-gothic \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
USER seluser  

