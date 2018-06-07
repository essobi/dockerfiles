FROM plone:4  
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-
alerts@googlegroups.com>  
  
USER root  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends build-essential \  
&& rm -rf /var/lib/apt/lists/*  
USER plone  
  
COPY site.cfg /plone/instance/  
RUN bin/buildout -c site.cfg  

