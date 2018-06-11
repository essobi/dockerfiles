FROM iammer/dev-node  
ADD entrypoint.sh /  
RUN su -c '\  
source $HOME/.nvm/nvm.sh &&\  
nvm install 8 &&\  
nvm use 8 &&\  
cd /tmp &&\  
git clone https://github.com/iammer/wetty &&\  
cd wetty &&\  
NODE=$(ls -1 -d /home/michael/.nvm/versions/node/* | sort | tail -n 1) &&\  
PATH=$PATH:$NODE/bin &&\  
npm install \  
' michael &&\  
mv /tmp/wetty /srv &&\  
chown -R root:root /srv/wetty  
  
CMD ["/entrypoint.sh"]  
  

