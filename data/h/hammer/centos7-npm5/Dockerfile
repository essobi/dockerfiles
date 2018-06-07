From centos:7  
MAINTAINER "takemi.ohama" <takemi.ohama@ietty.co.jp>  
  
RUN echo -e "[google-chrome]\nname=google-
chrome\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-
ssl.google.com/linux/linux_signing_key.pub" > /etc/yum.repos.d/google-
chrome.repo  
  
RUN yum -y update && yum -y upgrade  
RUN yum -y install epel-release  
RUN yum -y install npm wget git sudo bzip2 which \  
gcc gcc-c++ make flex bison gperf ruby \  
openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \  
libpng-devel libjpeg-develi xorg-x11-server-Xvfb google-chrome-stable.x86_64 \  
liberation-mono-fonts liberation-narrow-fonts liberation-sans-fonts
liberation-serif-fonts  
  
#npmとnodeを最新版に更新  
RUN npm cache clean  
RUN npm install --no-progress -g n  
RUN n 7.10.1  
RUN npm install --no-progress -g yarn typings typescript @angular/cli  
RUN yarn global add npm@5.3.0  
  
RUN adduser docker && \  
usermod -G wheel,users docker && \  
usermod -G users root && \  
chmod g+sw /opt && \  
echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \  
sed -i -e "s/Defaults requiretty/#Defaults requiretty/" /etc/sudoers  
  
RUN echo 'export DISPLAY=:99' >> /etc/profilei && \  
echo 'export CHROME_BIN=/usr/bin/google-chrome-stable' >> /etc/profile && \  
echo 'export PATH=/usr/local/bin:$PATH' >> /etc/profile && \  
echo 'export PATH=/usr/local/bin:$PATH' >> /root/.bashrc  
  
#/optはvolumesで利用するので便宜的に移動  
RUN mv /opt/google /var/lib && \  
rm -f /usr/bin/google-chrome-stable && \  
ln -s /var/lib/google/chrome/google-chrome /usr/bin/google-chrome-stable  
  
USER docker  
WORKDIR /home/docker  
  
ENV DISPLAY=:99  
ENV CHROME_BIN=/usr/bin/google-chrome-stable  
  
EXPOSE 3000 3001 1080  
CMD ["tail","-f","/dev/null"]  

