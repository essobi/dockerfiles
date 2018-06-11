FROM ubuntu  
RUN apt-get update && apt-get -y install sudo && sudo apt-get install curl -y
&& sudo apt-get install git -y  
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - && sudo
apt-get install -y nodejs && sudo apt-get update -y && sudo apt-get upgrade -y
&& sudo apt-get install -y build-essential nodejs  
RUN sudo npm install -g ethereumjs-testrpc truffle && sudo chown -R $(whoami)
~/.npm && sudo chown -R $USER:$(id -gn $USER) ~/.config  
RUN npm install ethereumjs-testrpc web3@0.20.1 && npm install solc

