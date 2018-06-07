FROM iammer/dev-base  
  
RUN sudo apt install -y build-essential &&\  
su -c '\  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh
| bash &&\  
source ~/.nvm/nvm.sh &&\  
nvm install node &&\  
npm install -g ember-cli grunt supervisor bower \  
' michael  

