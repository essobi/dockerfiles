#  
# coomy/develop:node  
#  
FROM coomy/ubuntu:14.04  
MAINTAINER Coomy Chang <coomysky@gmail.com>  
  
  
##### System update and install  
RUN sudo apt-get update -qq && sudo apt-get upgrade -qq  
RUN sudo apt-get install -qqy build-essential libssl-dev libmysqlclient-dev  
  
##### Node installation  
RUN curl --location https://raw.github.com/creationix/nvm/master/install.sh |
sh  
RUN sudo /bin/bash -c "echo \"[[ -s \$HOME/.nvm/nvm.sh ]] && .
\$HOME/.nvm/nvm.sh\" >> /etc/profile.d/npm.sh"  
RUN echo "[[ -s $HOME/.nvm/nvm.sh ]] && . $HOME/.nvm/nvm.sh" >> $HOME/.bashrc  
  
##### Environment  
ENV PATH /home/ubuntu/.nvm/bin:$PATH  
RUN mkdir -p $HOME/code  
  
COPY run.bash $HOME/start/  
  
##### Clean  
RUN sudo apt-get clean  
RUN sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/bin/bash", "/home/ubuntu/start/run.bash"]  

