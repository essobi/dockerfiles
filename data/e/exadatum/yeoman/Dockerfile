###############################################################################  
# Header Documentation #  
###############################################################################  
#  
# Dockerfile to create container with following tools  
# - Yeoman  
# - Yeoman Karma Generator  
# - Yeoman Angular Generator  
# - Yeoman JHipster Generator  
# - Bower  
# - Grunt-Cli  
# - Gulp  
#  
###############################################################################  
# Header #  
###############################################################################  
  
FROM ubuntu:14.04  
  
MAINTAINER ExaDatum <support@exadatum.com>  
  
  
###############################################################################  
# Environment Variables #  
###############################################################################  
  
# Tar files for pythong and nodejs are downloaded to tmp directory  
ENV TMP_DIR /tmp  
  
# Docker user to be created to intereact with container. This user is  
# different than root  
ENV DOCKER_USER=docker  
  
# Password for the user defined by DOCKER_USER environment  
# variable  
ENV DOCKER_USER_PASSWORD=docker  
  
# Password for the root  
ENV ROOT_USER_PASSWORD=root  
  
###############################################################################  
# Instructions #  
###############################################################################  
  
# Install dependencies  
# wget is required to download python and npm tar files  
# build-essential is required for npm  
# Others are required for building python 2.7.5  
RUN apt-get update && apt-get install -y wget build-essential  
RUN apt-get install -y libreadline-gplv2-dev libncursesw5-dev  
RUN apt-get install -y libssl-dev libsqlite3-dev tk-dev  
RUN apt-get install -y libgdbm-dev libc6-dev libbz2-dev  
  
# Set the current work directory to /tmp directory  
WORKDIR ${TMP_DIR}  
  
# Download python 2.7.5 tar.  
# It will be downloaded to temp directory which is current work directory  
RUN wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz  
  
# Extract downloaded python tar file in previous step.  
# It will be extracted to Python-2.7.5 directory which is inside /tmp
directory  
RUN tar -xf Python-2.7.5.tgz  
  
# To build python, change the current working directory to directory where  
# python source code is extracted.  
WORKDIR ${TMP_DIR}/Python-2.7.5/  
  
#Build python 2.7.5 source code and install it  
RUN ./configure  
RUN make  
RUN make install  
  
# Change the current work directory back to /tmp directory  
WORKDIR ${TMP_DIR}  
  
# Download nodejs 0.12.2 tar.  
# It will be downloaded to temp directory which is current work directory  
RUN wget https://github.com/joyent/node/archive/v0.12.2.tar.gz  
  
# Extract downloaded nodejs tar file in previous step.  
# It will be extracted to node-0.12.2 directory which is inside /tmp directory  
RUN tar -xf v0.12.2.tar.gz  
  
# To build nodejs, change the current working directory to directory where  
# nodejs source code is extracted.  
WORKDIR ${TMP_DIR}/node-0.12.2/  
  
#Build nodejs 0.12.2 source code and install it  
RUN ./configure  
RUN make  
RUN make install  
  
# Install following components using npm  
# - Yeoman  
# - Yeoman Karma Generator  
# - Yeoman Angular Generator  
# - Yeoman JHipster Generator  
# - Bower  
# - Grunt-Cli  
# - Gulp  
RUN npm install -g yo bower grunt-cli gulp generator-karma  
RUN npm install -g generator-angular generator-jhipster  
  
# Set the root password  
RUN echo "root:${ROOT_USER_PASSWORD}" | chpasswd  
  
# Create new user called define by DOCKER_USER environment variable  
# which will be able to work with yeoman.  
# Following issue prohibits using root with yo command  
# https://github.com/yeoman/yeoman.io/issues/282  
RUN adduser --disabled-password --shell /bin/bash --gecos '' ${DOCKER_USER}  
  
# Add user defined by DOCKER_USER environment variable to the sudoers list  
RUN adduser ${DOCKER_USER} sudo  
  
# Set the work directory to home dir of the root  
WORKDIR /home/${DOCKER_USER}  
  
# Set the user id  
USER ${DOCKER_USER}  
  
# Start bash  
CMD ["/bin/bash"]  
  
###############################################################################  
# End #  
###############################################################################  
  
  

