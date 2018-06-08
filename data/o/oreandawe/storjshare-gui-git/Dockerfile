FROM debian  
RUN apt-get update  
RUN apt-get install -qqy libasound2  
RUN apt-get install -qqy libgconf-2-4  
RUN apt-get install -qqy libgtk2.0-0  
RUN apt-get install -qqy libnss3  
RUN apt-get install -qqy libxss1  
RUN apt-get install -qqy libxtst6  
RUN apt-get install -qqy wget  
RUN apt-get install -qqy x11-apps  
# Make sure sh points to bash.  
RUN ln -sf /bin/bash /bin/sh  
  
RUN apt-get install -qqy git  
RUN apt-get install -qqy nodejs  
RUN ln -sf nodejs /usr/bin/node  
RUN apt-get install -qqy node-gyp  
RUN apt-get install -qqy npm  
  
RUN git clone https://github.com/Storj/storjshare-gui.git  
WORKDIR /storjshare-gui/app  
RUN npm install  
WORKDIR /storjshare-gui  
RUN npm install  
  
ENV DISPLAY :0  
ENTRYPOINT ["npm"]  
CMD ["start"]  

