FROM maven:3.3.3-jdk-8  
ENV HOME_DIR=/usr/src/app  
  
WORKDIR /tmp  
  
RUN wget http://thelinuxbox.org/downloads/fonts/msttcorefonts.tar.gz && \  
tar -zxvf msttcorefonts.tar.gz && \  
mkdir -p /usr/share/fonts/TTF/ && \  
cp msttcorefonts/*.ttf /usr/share/fonts/TTF/ && \  
fc-cache -fv  
  
  
WORKDIR ${HOME_DIR}

