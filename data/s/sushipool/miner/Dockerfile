FROM ubuntu:16.04  
ENV REPO='https://github.com/Sushipool/miner.git'  
ENV HOME='/home/root'  
ENV WALLET='NQ04 3F73 CHG5 RCBH CDMM MR5C RNJV 0N6J CXJR'  
ENV SERVER='eu.sushipool.com'  
ENV NAME='sushipool_miner'  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python build-essential git curl  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x -o nodesource_setup.sh &&
bash nodesource_setup.sh  
RUN apt-get -y install nodejs  
  
# curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
# echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
# sudo apt-get update && sudo apt-get install yarn  
RUN npm install -g gulp  
  
# RUN mkdir -p $HOME  
WORKDIR $HOME  
RUN git clone ${REPO}  
RUN cd $HOME/miner/miner && npm install --unsafe  
  
WORKDIR $HOME/miner/miner  
CMD ["sh", "-c", "node index.js --address=\"${WALLET}\" --server=${SERVER}
\--name=${NAME}"]  
# CMD ["/bin/bash"]

