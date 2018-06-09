FROM ubuntu:14.04  
MAINTAINER TaopaiC <pctao.tw@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-add-repository -y ppa:chris-lea/node.js && \  
add-apt-repository -y "deb http://archive.canonical.com/ $(lsb_release -sc)
partner" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release
-sc) multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release
-sc)-updates multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release
-sc)-backports main restricted universe multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release
-sc)-security main restricted universe multiverse" && \  
dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get clean  
  
RUN apt-get install -y xvfb x11-xkb-utils xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic \  
python-pip redis-server &&\  
apt-get clean  
  
RUN apt-get install -y nodejs skype git &&\  
apt-get clean  
  
RUN npm install -g hubot coffee-script  
RUN hubot --create hubot-skype  
WORKDIR hubot-skype  
RUN pip install Skype4Py  
RUN npm install && npm install --save git://github.com/netpro2k/hubot-
skype.git  
ENV HUBOT_NAME hubot  
# ENV SKYPE_USERNAME  
# ENV SKYPE_PASSWORD  
ADD data/shared.xml /.Skype/shared.xml  
ADD data/hubot-run.sh /hubot-skype/hubot-run.sh  
ADD hubot-scripts.json /hubot-skype/hubot-scripts.json  
VOLUME ["/var/lib/redis"]  
EXPOSE 8080  
ONBUILD ADD hubot-scripts.json /hubot-skype/hubot-scripts.json  
ONBUILD ADD dep.txt /hubot-skype/dep.txt  
ONBUILD RUN cat /hubot-skype/dep.txt | xargs npm install --save  
  
CMD xvfb-run /bin/sh /hubot-skype/hubot-run.sh  

