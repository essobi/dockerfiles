FROM eeacms/kgs-devel  
MAINTAINER "EEA: IDM2 B-Team"  
RUN curl -o /plone/instance/buildout.cfg -SL
https://raw.githubusercontent.com/eea/eea.docker.plone-
esdrt/master/buildout.cfg \  
&& buildout -c devel.cfg  

