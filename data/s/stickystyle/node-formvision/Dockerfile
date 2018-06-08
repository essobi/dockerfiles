FROM pritunl/archlinux:latest  
  
RUN pacman --noconfirm -S base-devel \  
git \  
nodejs \  
npm \  
python2  
RUN npm config set python /usr/bin/python2  
RUN npm install -g coffee-script  
RUN git clone https://github.com/stickystyle/node-fv.git  
WORKDIR node-fv  
RUN npm install -g  

