# Seebis Base Ubuntu Dockerfile  
#  
# https://github.com/seebi/ubuntu.docker  
FROM ubuntu:17.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential devscripts debhelper && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget make zsh exuberant-
ctags  
  
# Install zsh config  
RUN \  
mkdir -p /root/.config/ /root/.cache/ && \  
git clone https://github.com/seebi/zshrc.git /root/.config/zsh/ && \  
cd /root/.config/zsh && \  
make install && \  
chsh -s /usr/bin/zsh root && \  
rm -f /root/.zshrc && ln -s /root/.config/zsh/zshrc /root/.zshrc && \  
echo "RUN DONE"  
  
# Set environment variables.  
ENV HOME /root  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["byobu"]  

