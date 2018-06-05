FROM python:2.7-onbuild  
MAINTAINER Thierry Valero (IRD/MIVEGEC)  
  
LABEL ird.mivegec.name='tvalero/web-asset-server'  
LABEL ird.mivegec.description='Specify Web Asset Server in a container'  
LABEL ird.mivegec.torun='docker run -it -d tvalero/web-asset-server:dev -v
<Your data volume>:/home/specify/attachments:rw'  
  
RUN apt-get update && apt-get install -y \  
imagemagick \  
ghostscript  
  
ENV SPECIFY_KEY None  
ENV SPECIFY_HOST localhost  
  
ENV SPECIFY_PORT 8080  
EXPOSE 8080  
ENV BASE_DIR /home/specify/attachments/  
RUN mkdir -p /home/specify/attachments  
VOLUME /home/specify/attachments  
  
ENTRYPOINT python server.py  

