FROM makeorg/docker-sbt-coursier  
  
MAINTAINER flaroche@gmail.com  
  
# Let's run stuff  
RUN \  
touch /root/.profile && \  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh |
bash && \  
. /root/.profile && nvm install v6.10.2 && nvm alias default v6.10.2  
  
RUN pacman -Sy --noconfirm && pacman -S archlinux-keyring --noconfirm &&
pacman -S yarn --noconfirm  
ENV LANG=en_US.UTF-8  
CMD ["/usr/bin/bash"]  

