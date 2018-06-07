FROM node:latest  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y \  
imagemagick \  
inkscape \  
make \  
texlive-full  
RUN npm install madoko -g  
RUN npm install madoko-local -g  
RUN apt-get install -y \  
inotify-tools \  
xzdec  
RUN tlmgr init-usertree  
COPY add_user add_user  
RUN ./add_user  
USER developer

