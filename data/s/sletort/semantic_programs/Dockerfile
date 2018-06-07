############################################################  
# Dockerfile to build semantic_programs tool container image  
# Based on debian Jessie/8  
############################################################  
  
# Set the base image to debian  
FROM debian:8  
  
RUN apt-get clean -y  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
################## DEPENDENCIES INSTALLATION ######################  
ENV PACKAGES curl git python2.7  
  
RUN apt-get install -y ${PACKAGES}  
  
WORKDIR /usr/bin  
RUN ln -s python2.7 python  
  
#### program_description INSTALLATION => for Prov-O trace #########  
ENV DIR /opt  
WORKDIR ${DIR}  
  
## get code source  
#--- from git repo  
ENV GIT https://gitlab.irisa.fr/semantic_programs/Program_Descriptions.git  
RUN git clone --recursive ${GIT}  
ENV SOURCE_DIR Program_Descriptions  
  
#--- /from git repo  
  
## installation commands  
RUN ln -s $DIR/$SOURCE_DIR/*.py /usr/local/bin/  
RUN export PYTHON_PATH=$PYTHON_PATH:$DIR/$SOURCE_DIR/lib  
  
ENV DESCR_DIR /opt/descr  
RUN mkdir $DESCR_DIR  
RUN cp $DIR/$SOURCE_DIR/data/parse_description.json $DESCR_DIR/  
  
## test commands  
RUN parse_description.py --mode docker $DESCR_DIR/parse_description.json  
  
################## Dockerfile usage ######################  
## the command launched by default when running the container  
ENTRYPOINT ["parse_description.py"]  
CMD ["--help"]  
  
################## METADATA ######################  
MAINTAINER "sletort"  
  

