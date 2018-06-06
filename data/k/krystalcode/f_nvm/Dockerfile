FROM krystalcode/f_fedora  
  
ENV NVM_VERSION 0.33.2  
  
# Install OS packages required.  
# Install "git", "make" and "gcc-c++", required by "npm" for installing some  
# packages.  
RUN dnf -y install git make gcc-c++ && \  
dnf clean all && \  
# Install "nvm".  
curl -o\-
https://raw.githubusercontent.com/creationix/nvm/v{$NVM_VERSION}/install.sh |
bash  

