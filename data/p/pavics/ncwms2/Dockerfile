# vim:set ft=dockerfile:  
FROM birdhouse/bird-base:latest  
MAINTAINER https://github.com/bird-house/birdhouse-
playground/tree/master/ncwms2  
  
LABEL Description="ncWMS2 Web Map Service" Vendor="Reading eScience Centre"
Version="2.2.2"  
  
# Configure hostname and user for services  
ENV HOSTNAME localhost  
ENV USER www-data  
  
  
# Set current home  
ENV HOME /root  
  
# Copy application sources  
COPY . /opt/birdhouse  
  
# cd into application  
WORKDIR /opt/birdhouse  
  
# Provide custom.cfg with settings for docker image  
COPY .docker.cfg custom.cfg  
  
# Install system dependencies  
RUN bash bootstrap.sh -i && bash requirements.sh  
  
# Set conda enviroment  
ENV ANACONDA_HOME /opt/conda  
ENV CONDA_ENVS_DIR /opt/conda/envs  
  
# Run install  
RUN make clean install  
  
# Volume for data, cache, logfiles, ...  
RUN chown -R $USER $CONDA_ENVS_DIR/birdhouse  
RUN mkdir -p $CONDA_ENVS_DIR/birdhouse/var/lib && mv
$CONDA_ENVS_DIR/birdhouse/var/lib /data && ln -s /data
$CONDA_ENVS_DIR/birdhouse/var/lib  
RUN chown -R $USER /data  
VOLUME /data  
  
# Ports used in birdhouse  
EXPOSE 8080  
# Start supervisor in foreground  
ENV DAEMON_OPTS --nodaemon --user $USER  
# Start service ...  
CMD ["make", "update-config", "update-user", "start"]  
  

