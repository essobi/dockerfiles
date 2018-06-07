FROM eeacms/kgs-devel  
MAINTAINER "EEA: IDM2 B-Team"  
RUN curl -o /plone/instance/buildout.cfg -SL
https://raw.githubusercontent.com/eea/eea.docker.plone-eni-
seis/master/buildout.cfg \  
&& buildout -c devel.cfg  

