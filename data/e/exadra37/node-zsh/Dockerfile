FROM node:latest  
  
LABEL "com.exadra37.vendor"="Exadra37"  
LABEL com.exadra37.package-name="exadra37-docker-images/dockerize-visual-
studio-code"  
LABEL description="Node official image with ZSH+OhMyZSH with GIT and CURL."  
  
# Will not prompt for questions  
ARG DEBIAN_FRONTEND=noninteractive  
  
# The official image as a user called "node" that as the UID 1000.  
# Once the UID 1000 normally will match the one used in our OS, than we will
avoid permissions issues when mapping  
# volumes between the host and container.  
ARG CONTAINER_USER="node"  
WORKDIR /home/"${CONTAINER_USER}"  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
  
# Install Required Dependencies  
apt-get -y install \  
zsh \  
curl \  
git && \  
  
# Force installation of missing dependencies  
apt-get -y -f install && \  
  
# Install Oh My Zsh for Root and Node user  
bash -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)" && \  
chsh -s /usr/bin/zsh && \  
cp -R /root/.oh-my-zsh /home/"${CONTAINER_USER}" && \  
cp /root/.zsh* /home/"${CONTAINER_USER}" && \  
sed -i "s/\/root/\/home\/${CONTAINER_USER}/g" /home/"${CONTAINER_USER}"/.zshrc
&& \  
chown -R "${CONTAINER_USER}":"${CONTAINER_USER}" /home/"${CONTAINER_USER}" &&
\  
  
# cleaning  
rm -rvf /var/lib/apt/lists/*  
  
CMD ["zsh"]  

