FROM node:6  
MAINTAINER Lars Modig <larswillymodig@gmail.com>  
  
RUN git clone https://github.com/Spiritdude/OpenJSCAD.org.git /openjscad \  
&& mkdir /input /output  
  
COPY package.json /entry/  
RUN cd /entry && npm install  
  
COPY entry.js /entry/  
  
CMD node /entry  

