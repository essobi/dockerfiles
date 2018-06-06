FROM debian:jessie  
ENV DEBIAN_FRONTEND noninteractive  
ENV APT_LISTCHANGES_FRONTEND noninteractive  
WORKDIR /root  
RUN apt-get update  
RUN apt-get install -y wget git build-essential  
RUN echo "deb http://files.freeswitch.org/repo/deb/debian jessie main" >
/etc/apt/sources.list.d/99FreeSWITCH.list  
RUN wget http://files.freeswitch.org/repo/deb/debian/key.gpg  
RUN apt-key add key.gpg  
RUN apt-get update  
RUN git config --global pull.rebase true  
WORKDIR /usr/src  
RUN git clone https://freeswitch.org/stash/scm/fs/freeswitch.git  
WORKDIR /usr/src/freeswitch  
RUN git checkout v1.6.7  
WORKDIR /usr/src/freeswitch/html5/verto/verto_communicator/  
RUN apt-get update  
RUN apt-get install -y --force-yes npm nodejs-legacy  
RUN npm install -g grunt grunt-cli bower  
RUN npm install  
RUN bower --allow-root install  
RUN grunt build  
VOLUME /usr/src/freeswitch/html5/verto/verto_communicator/  
RUN mkdir -p /verto  
ENTRYPOINT cp -r /usr/src/freeswitch/html5/verto/verto_communicator/dist/.
/verto  
  

