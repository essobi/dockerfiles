# vim:set ft=dockerfile:  
FROM birdhouse/bird-base:latest  
MAINTAINER https://github.com/bird-house/birdhouse-
playground/tree/master/mongodb  
  
LABEL Description="MongoDB NoSQL Database" Vendor="MongoDB" Version="3.3.9"  
  
# Configure hostname and user for services  
ENV HOSTNAME localhost  
ENV USER www-data  
  
  
# Set current home  
ENV HOME /root  
  
# Load sources from github  
RUN mkdir -p /opt/birdhouse && curl -ksL https://github.com/bird-
house/birdhouse-playground/archive/master.tar.gz | tar -xzC /opt/birdhouse
--strip-components=1  
  
WORKDIR /opt/birdhouse/mongodb  
  
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
EXPOSE 27027  
# Start supervisor in foreground  
ENV DAEMON_OPTS --nodaemon --user $USER  
# Start service ...  
CMD ["make", "start"]  
  

