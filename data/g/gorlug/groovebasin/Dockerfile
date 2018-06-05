FROM ubuntu:16.04  
MAINTAINER Achim Rohn <achim@rohn.eu>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install nodejs-dev
nodejs-legacy npm git ffmpeg libspeexdsp-dev libebur128-dev libsoundio-dev
libchromaprint-dev libgroove-dev libgrooveplayer-dev libgrooveloudness-dev
libgroovefingerprinter-dev  
RUN useradd -m groovebasin && \  
mkdir /home/groovebasin/music && \  
mkdir /home/groovebasin/groove && \  
chown -R groovebasin:groovebasin /home/groovebasin  
USER groovebasin  
RUN git clone \--branch album-cover https://github.com/gorlug/groovebasin.git
/home/groovebasin/groovebasin  
WORKDIR /home/groovebasin/groovebasin/  
RUN npm run build  
RUN npm start ; exit 0  
RUN sed -i 's/ "host": "127.0.0.1",/ "host": "0.0.0.0",/g' config.json  
RUN sed -i 's/ "albumArt": false/ "albumArt": true/g' config.json  
RUN sed -i 's| "musicDirectory": "/home/groovebasin",| "musicDirectory":
"/home/groovebasin/music",|g' config.json  
RUN ln -s /home/groovebasin/groove groovebasin.db  
ENV HOME /home/groovebasin  
WORKDIR /home/groovebasin/groovebasin  
  
EXPOSE 16242  
EXPOSE 6600  
ENTRYPOINT ["npm", "start"]  

