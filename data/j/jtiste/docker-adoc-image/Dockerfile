# Dockerfile for Asciidocto generation needs  
## Need Maven in order to generate pdf  
FROM maven:3.3.9-alpine  
  
## plantuml schema could be generated but need graphviz package !  
## schema gen process rise Exception related to font ! to correct this, we
need to install ttf-dejavu package  
RUN apk update && \  
apk add \--update graphviz && \  
apk add \--update ttf-dejavu  
  
## Change the default TMP DIR  
## correct issue from asciidoctors since version 1.5.6 is in use
(asciidoctorj.diagram 1.5.4.1)  
RUN export TMPDIR=~/tmp && mkdir $TMPDIR && chmod 777 $TMPDIR  
WORKDIR ~/tmp  

