FROM ubuntu:16.04  
MAINTAINER Kacper Sokol <ks1591@bristol.ac.uk>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
RUN apt-get update \  
&& apt-get upgrade -y  
  
RUN apt-get install -y \  
git \  
python \  
python-pip \  
nodejs \  
nodejs-legacy \  
npm  
  
ENV SHELL /bin/bash  
ENV HYPERSTREAM_USER jovyan  
ENV HYPERSTREAM_UID 1000  
ENV HOME /home/$HYPERSTREAM_USER  
ENV HYPERSTREAM_DIR $HOME/hyperstream  
  
# Create jovyan user with UID=1000 and in the 'users' group \ -N -u $SWISH_UID  
RUN useradd -m -s $SHELL $HYPERSTREAM_USER  
  
RUN mkdir -p $HYPERSTREAM_DIR \  
&& chown $HYPERSTREAM_USER $HYPERSTREAM_DIR  
  
USER $HYPERSTREAM_USER  
  
RUN git clone \--depth=1 https://github.com/IRC-SPHERE/HyperStreamViewer.git
$HYPERSTREAM_DIR  
RUN pip install --user -r $HYPERSTREAM_DIR/requirements.txt  
  
USER root  
RUN npm -g install bower  
USER $HYPERSTREAM_USER  
  
WORKDIR $HYPERSTREAM_DIR  
RUN bower update  
  
# Configure mongo host  
RUN ./config_local.sh  
RUN sed -i -e 's/localhost/hyperstream-mongo/g' hyperstream_config.json  
  
EXPOSE 5000  
# Run HyperStreamViewer  
ENTRYPOINT python server.py  

