FROM luckyqm/nodenvm:v4  
LABEL MAINTAINER="Qi Ma <mq@tuojie.com>"  
LABEL VERSION="1.0"  
  
WORKDIR $HOME/  
VOLUME /data  
RUN source $HOME/.bashrc  
RUN echo $HOME  
RUN . $HOME/.nvm/nvm.sh && command -v nvm  
RUN . $HOME/.nvm/nvm.sh && nvm use default \  
&& npm install bitcore -g --user "lucky"  

