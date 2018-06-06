FROM node:boron  
  
#install ffmpeg  
RUN mkdir /ffmpeg \  
&& cd /ffmpeg \  
&& wget http://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz
\  
&& tar xf ffmpeg-git-64bit-static.tar.xz \  
&& cd ./ffmpeg* \  
&& mv * ../ \  
&& ln -s /ffmpeg/ffmpeg /usr/bin/ffmpeg \  
&& ln -s /ffmpeg/ffprobe /usr/bin/ffprobe \  
&& ln -s /ffmpeg/ffserver /usr/bin/ffserver  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
# Let's make sure the app built correctly  
RUN ffmpeg -buildconf  
  
# Make sure Node.js is installed  
RUN node -v  
RUN npm -v  
  
CMD [ "npm", "start" ]  

