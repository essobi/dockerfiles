FROM node:argon  
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>  
  
# inspired by https://github.com/sauercrowd/kitematic-
docker/blob/master/Dockerfile  
RUN apt-get update \  
&& apt-get install -y git libgtk2.0-0 libnotify4 libnotify-dev libgconf-2-4
libnss3 libasound2 libcanberra-gtk3-module  
#xorg  
# install desired node version, see .travis.yml  
ENV NODE_VERSION 4.1.1  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash  
ENV NVM_DIR=$HOME/.nvm  
RUN . $HOME/.nvm/nvm.sh && nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
WORKDIR /kitematic  
RUN git clone \--depth 1 -b model-ui https://github.com/nuest/kitematic
/kitematic \  
&& npm install \  
&& touch /root/.Xauthority  
  
ENTRYPOINT ["npm", "start" ]  
  
# BUILD  
#  
# docker build --tag kitematic-modeller .  
# USE  
#  
# xhost +  
# docker run --net host --name kitematic -v /tmp/.X11-unix:/tmp/.X11-unix -e
DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority -e uid=$(id -u) -e
gid=$(id -g) -v /var/run/docker.sock:/var/run/docker.sock kitematic-modeller  
# xhost -  
#  
# more options that were tried:  
# - -d  
# - --privileged=true  
# - --security-opt seccomp:unconfined (not recommended but can get rid of the
libudev error message that way, see https://github.com/msokk/electron-render-
service/issues/9#issuecomment-184404354

