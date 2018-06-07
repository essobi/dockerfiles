# @package exadra37-docker-images/dockerize-graphical-user-interface-app  
# @link https://gitlab.com/u/exadra37-docker-images/dockerize-graphical-user-
interface-app  
# @since 11 March 2017  
# @license GPL-3.0  
# @author Exadra37(Paulo Silva) <exadra37ingmailpointcom>  
#  
# Social Links:  
# @link Auhthor: https://exadra37.com  
# @link Gitlab: https://gitlab.com/Exadra37  
# @link Github: https://github.com/Exadra37  
# @link Linkedin: https://uk.linkedin.com/in/exadra37  
# @link Twitter: https://twitter.com/Exadra37  
###################################################################################  
# #  
# ATTENTION: #  
# #  
# TO DOCKERIZE A GUI APP, PLEASE CREATE ANOTHER DOCKERFILE TO EXTEND THIS
ONE... #  
# #  
###################################################################################  
FROM ubuntu:latest  
  
LABEL "com.exadra37.vendor"="Exadra37"  
LABEL com.exadra37.package-name="exadra37-docker-images/dockerize-graphical-
user-interface-app"  
LABEL version="0.0.1.0"  
LABEL description="Dockerize any App with a graphical user interface. \  
This allow us to run the Dockerized APP from inside a Docker Container. \  
  
Advantages: \  
* No need to install the APP in our Operating System to try it. \  
* Try the APP with many different setups without be afraid to break our OS. \  
* More secure to run, once we can destroy the container when finished, therefore if is compromised it will not \  
infect the OS in our computer. \  
* Keep our OS clean and free of bloated APPs, making easy to upgrade it at any time. \  
"  
  
# Removes DBUS warning that should be only seen by Developer  
# https://bugs.launchpad.net/ubuntu/+source/at-spi2-core/+bug/1193236  
ENV NO_AT_BRIDGE=1  
# Will not prompt for questions  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Why we want to be able to override?  
# - Because this Dockerfile main purpose is to be used by Bash scripts to
dynamical build local images to Dockerize  
# some GUI apps like Visual Studio Code, Sublime Text 3 and many others
ones...  
# - But this Dockefile will be also used to build the Docker Image, with this
defaults, to be hosted in Docker Hub.  
#  
# Override with docker build --build-arg key=value  
ARG CONTAINER_USER="${CONTAINER_USER:-dockerize}"  
ARG CONTAINER_UID="${CONTAINER_UID:-2000}"  
ARG CONTAINER_ENTRYPOINT="${CONTAINER_ENTRYPOINT:-'./entrypoint.sh'}"  
ARG CONTAINER_LANG="${CONTAINER_LANG:-'en_GB:en'}"  
ARG CONTAINER_LOCALE="${CONTAINER_LOCALE:-'en_GB.UTF-8'}"  
ARG CONTAINER_SHELL="${CONTAINER_SHELL:-'/usr/bin/zsh'}"  
ARG
HOST_SETUP_USER_SHELL_FILE="${HOST_SETUP_USER_SHELL_FILE:-~/.dockerize/setup-
user-shell.sh}"  
# Use this script to setup your preferred Shell...  
#  
# Why customize a Shell in a Docker Image to Dockerize a GUI?  
# - For example when dockerizing Visual Studio Code we can access the Shell
from inside the editor.  
COPY ./setup-user-shell.sh /.container/setup-user-shell.sh  
  
# DOCKER RUNS ALL SHELL COMANDS WITH: /bin/sh  
RUN apt-get update && \  
apt-get -y upgrade && \  
  
# Installs Required Dependencies...  
#  
# This is the minimal dependencies to be able to run a GUI app from inside a
Docker Container.  
#  
# Keep in mind that you still need to install more dependencies depending in
what GUI app you are trying to Dockerize.  
#  
# For Example to Dockerize Gedit editor we need at least more 2 dependencies:  
# * libcanberra-gtk3-module \  
# * gedit \  
#  
# Never EDIT this Dockerfile... instead create a new one and extend from this
one.  
#  
# See project https://gitlab.com/exadra37-dockerize-vscode for an example  
apt-get -y install \  
ca-certificates \  
apt-utils \  
dbus-x11 && \  
  
# Force installation of missing dependencies  
apt-get -y -f install && \  
  
# Localization  
locale-gen "${CONTAINER_LOCALE}" && \  
  
# Add $CONTAINER_USER  
#  
# If the GUI App being Dockerized needs a Sudo User, please set it in the
image that will extend from this one  
# to Dockerize it.  
useradd -m -u "${CONTAINER_UID}" -s "${CONTAINER_SHELL}" "${CONTAINER_USER}"
&& \  
echo "${CONTAINER_USER}:${CONTAINER_USER}" | chpasswd && \  
  
  
# Setup Shell for $CONTAINER_USER  
# If the Shell is not Bash or Sh we need to install it from
$HOST_SETUP_USER_SHELL_FILE  
# For ZSH shell a default installation is provided in the script we are
invoking...  
bash ./.container/setup-user-shell.sh "${CONTAINER_USER}" "${CONTAINER_SHELL}"
"${HOST_SETUP_USER_SHELL_FILE}" && \  
  
# We must create .config, .cache and .local folders specifying the container
user or we end up with it belonging to root user  
su "${CONTAINER_USER}" -c 'mkdir /home/"${CONTAINER_USER}"/.config' && \  
su "${CONTAINER_USER}" -c 'mkdir /home/"${CONTAINER_USER}"/.cache' && \  
su "${CONTAINER_USER}" -c 'mkdir -p /home/${CONTAINER_USER}/.local/share' && \  
  
# Cleaning  
rm -rvf /var/lib/apt/lists/*  
  
# MUST BE SET AFTER RUN COMMAND  
ENV LANG "${CONTAINER_LOCALE}"  
ENV LANGUAGE "${CONTAINER_LANG}"  
ENV LC_ALL "${CONTAINER_LOCALE}"  
ENV SHELL "${CONTAINER_SHELL}"  
  
# Use this script to set what you want to happen when starting the container.  
COPY "${CONTAINER_ENTRYPOINT}"
/home/"${CONTAINER_USER}"/.container/entrypoint.sh  
  
# This must belong to the $CONTAINER_USER not to root user...  
RUN chown -R "${CONTAINER_USER}":"${CONTAINER_USER}"
/home/"${CONTAINER_USER}"/.container  

