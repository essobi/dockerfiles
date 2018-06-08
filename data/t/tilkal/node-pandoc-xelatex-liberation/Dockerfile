FROM node:8-slim  
  
ADD https://github.com/jgm/pandoc/releases/download/2.2/pandoc-2.2-1-amd64.deb
/tmp/  
  
RUN apt update && \  
apt upgrade -y && \  
apt install software-properties-common -y && \  
add-apt-repository ppa:texlive-backports/ppa && \  
apt install fontconfig bzip2 texlive texlive-xetex texlive-math-extra texlive-
fonts-recommended texlive-fonts-extra ttf-liberation -y && \  
npm -i g npm && \  
fc-cache -f -v && \  
dpkg -i /tmp/*.deb

