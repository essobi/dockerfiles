# Dockerfile  
FROM ryht/blankon:tambora  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 91824AB09120A048 && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
blankon-keyring  
RUN apt-get install -y \  
build-essential \  
curl \  
devscripts \  
equivs \  
git-buildpackage \  
git \  
lsb-release \  
make \  
openssh-client \  
pristine-tar \  
rsync \  
bzr \  
wget  
CMD ["/bin/bash"]  

