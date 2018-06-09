#!/bin/bash  
# @package exadra37-dockerize/visual-studio-code  
# @link https://gitlab.com/u/exadra37-dockerize/visual-studio-code  
# @since 5 March 2017  
# @license MIT  
# @author Exadra37(Paulo Silva) <exadra37ingmailpointcom>  
#  
# Social Links:  
# @link Auhthor: https://exadra37.com  
# @link Gitlab: https://gitlab.com/Exadra37  
# @link Github: https://github.com/Exadra37  
# @link Linkedin: https://uk.linkedin.com/in/exadra37  
# @link Twitter: https://twitter.com/Exadra37  
  
FROM exadra37/dockerize-graphical-user-interface-app  
  
LABEL "com.exadra37.vendor"="Exadra37"  
LABEL com.exadra37.package-name="exadra37-docker-images/dockerize-visual-
studio-code"  
LABEL version="0.0.1.1"  
LABEL description="Dockerize Visual Studio Code Editor."  
  
ARG CONTAINER_USER="${CONTAINER_USER:-vscode}"  
ARG CONTAINER_UID="${CONTAINER_UID:-3000}"  
ARG CONTAINER_SHELL="${CONTAINER_SHELL:-'/usr/bin/zsh'}"  
  
ARG VSC_DEB_FILE="vsc.deb"  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
  
# Install Required Dependencies  
apt-get -y install \  
libcanberra-gtk-module \  
libgconf-2-4 \  
libasound2 \  
libgtk2.0-0 \  
libxss1 && \  
  
# Force installation of missing dependencies  
apt-get -y -f install && \  
  
# Install Visual Studio Code  
curl -L 'https://go.microsoft.com/fwlink/?LinkID=760868' -o "${VSC_DEB_FILE}"
&& \  
dpkg -i -R "${VSC_DEB_FILE}" || echo "\n Will force install of missing Visual
Studio Code dependencies...\n" && \  
  
# Force installation of missing dependencies for Visual Studio Code  
apt-get -y -f install && \  
  
# Add Host User in Container  
useradd -m -u "${CONTAINER_UID}" -s "${CONTAINER_SHELL}" "${CONTAINER_USER}"
&& \  
echo "${CONTAINER_USER}:${CONTAINER_USER}" | chpasswd && \  
  
# Default Profile  
su "${CONTAINER_USER}" -c "/usr/bin/code --install-extension sleistner.vscode-
fileutils" && \  
  
# We need to copy .vscode dir because when Container is started, we use
--volume to map this dir in the Container to  
# another dir in the Host, so that we can persist all installed extensions
after Container is removed.  
#  
# This allows us to reuse the installed extensions across all Containers we
create, provided they are started  
# with the same Profile.  
#  
# Now that we have a copy we can put it back when the container starts... see
build/entrypoint.sh  
#  
# To Remember:  
# * .vscode dir on the HOST will contain only the extensions installed by us
during the use of Visual Studio Code.  
# * .vscode dir in the DOCKER IMAGE contains only the extensions installed
when build the Docker Image.  
# * .vscode dir on the CONTAINER is a merge of the HOST dir with the DOCKER
IMAGE dir during Container creation.  
su "${CONTAINER_USER}" -c 'mkdir -p /home/"${CONTAINER_USER}"/.container' && \  
su "${CONTAINER_USER}" -c 'cp -R /home/"${CONTAINER_USER}"/.vscode
/home/"${CONTAINER_USER}"/.container/.vscode' && \  
  
# Install Oh My Zsh for Root  
bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" && \  
chsh -s /usr/bin/zsh && \  
  
# Install Oh My Zsh for created $CONTAINER_USER  
su "${CONTAINER_USER}" -c 'bash -c "$(curl -fsSL
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"' && \  
chsh -s /usr/bin/zsh "${CONTAINER_USER}" && \  
  
# cleaning  
rm -rvf /var/lib/apt/lists/* && \  
rm -rvf "${VSC_DEB_FILE}"  
  
COPY ./entrypoint.sh /home/"${CONTAINER_USER}"/.container/vscode/entrypoint.sh  
  
RUN chown -R "${CONTAINER_USER}":"${CONTAINER_USER}"
/home/"${CONTAINER_USER}"/.container  

