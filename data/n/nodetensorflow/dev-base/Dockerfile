#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Pull base image.  
FROM ubuntu:14.04  
# This docker image belongs to the community.  
# This docker image has (or will have) more than one "maintainer", comment
your information  
#  
# Tony Ngan <tonynwk919@gmail.com>  
#  
MAINTAINER node-tensorflow  
  
ENV NODE_VER 4.2.2  
  
# Default install  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget python-pip python-
dev&& \  
rm -rf /var/lib/apt/lists/*  
  
# Automatically reload  
RUN echo 'export NVM_DIR="$HOME/.nvm"\n[ -s "$NVM_DIR/nvm.sh" ] && .
"$NVM_DIR/nvm.sh"' >> ~/.bashrc;  
  
# Install Node.js by nvm  
RUN /bin/bash -c \  
'git clone https://github.com/creationix/nvm.git ~/.nvm && \  
cd ~/.nvm && git checkout `git describe \--abbrev=0 v0.29.0` && \  
source ~/.nvm/nvm.sh && \  
nvm install $NODE_VER && \  
nvm alias default $NODE_VER && \  
# Install the npm packages below this line  
npm install -g node-gyp'  
  
# Install Tensorflow  
RUN pip install
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.5.0-cp27-none-
linux_x86_64.whl;  
  
ENTRYPOINT ["/bin/bash", "--login", "-i", "-c"]  
  
CMD ["bash"]  

