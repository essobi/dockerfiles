FROM node:boron  
  
# Create the app directory  
RUN wget
https://launchpad.net/ubuntu/+archive/primary/+files/ffmpeg_3.3.4.orig.tar.xz
\  
&& tar xvf ffmpeg_3.3.4.orig.tar.xz \  
&& cd ffmpeg-3.3.4 \  
&& apt-get update \  
&& apt-get -y install yasm libvpx-dev libx264. libmp3lame-dev libogg-dev
libvorbis-dev \  
&& ./configure --enable-libvpx --enable-libvorbis --enable-libx264 --enable-
libmp3lame --enable-gpl \  
\--enable-shared && make && make install  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json ./  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
RUN npm install  
  
# Bundle app source  
COPY . .  
  
# Bind app port to 8080  
EXPOSE 8888  
CMD ["npm", "start"]  

