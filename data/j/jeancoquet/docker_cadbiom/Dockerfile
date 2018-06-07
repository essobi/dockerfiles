############################################################  
# Dockerfile to build Cadbiom 1.1 container image  
# Based on debian Jessie/8  
############################################################  
  
# Set the base image to debian  
FROM debian:jessie  
  
ENV PACKAGES python2.7 python-pip python-gtksourceview2 python2.7-dev
libxml2-dev libxslt1-dev libxslt1-dev libgraphviz-dev pkg-config python-glade2
python-gtk2 python-tk  
  
ENV PIP_PACKAGES cadbiom-cmd  
  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y ${PACKAGES}  
  
################## CADBIOM INSTALLATION ######################  
  
RUN pip install ${PIP_PACKAGES}  
  
  
################## DOCKERFILE USAGE ######################  
ENTRYPOINT ["cadbiom_cmd"]  
CMD ["--help"]  

