# emacs  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
MAINTAINER Renzo Kottmann <renzo.kottmann@gmail.com>  
  
RUN apt-get update && \  
apt-get install --assume-yes \  
emacs24-lucid \  
emacs-goodies-el  
  
ENV APP_DIR=/workdir \  
USER=mate USER_ID=1000 \  
HOST_GROUP=boatswain HOST_GID=1496  
  
ENV HOME=/home/${USER}  
  
# perform setgid in mkdir and chmod in case future docker versions  
# support it  
RUN groupadd --gid "${HOST_GID}" "${HOST_GROUP}" && \  
useradd --create-home --shell /bin/bash \  
\--uid ${USER_ID} \--groups ${HOST_GROUP} ${USER} && \  
mkdir -m 775 -p ${APP_DIR} && \  
chown -R ${USER}:${USER} ${APP_DIR}  
  
# copying init file and packages  
COPY .emacs ${HOME}/  
COPY .emacs.d ${HOME}/.emacs.d  
  
# all files are copied as root therefore:  
RUN chown -R ${USER}:${USER} ${HOME}  
  
WORKDIR ${APP_DIR}  
VOLUME ${APP_DIR}  
  
USER ${USER}  
  
ENTRYPOINT ["/usr/bin/emacs", "--no-splash"]  

