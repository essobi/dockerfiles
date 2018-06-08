FROM nanobox/build:v1  
  
# Install zsh  
RUN apt-get update -qq && \  
apt-get install -y zsh && \  
apt-get clean all  
  
# add temporary scripts  
ADD scripts/. /var/tmp/  
  
# install oh my zsh  
RUN su - gonano -c "/var/tmp/install-oh-my-zsh.sh"  
  
# copy the .zshrc file  
COPY files/zshrc /home/gonano/.zshrc  
  
CMD [ "/opt/gonano/bin/nanoinit", "/bin/sleep", "365d" ]  

