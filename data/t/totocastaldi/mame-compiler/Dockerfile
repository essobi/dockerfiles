FROM ubuntu:16.04  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y git  
RUN apt-get install -y unzip  
RUN apt-get install -y build-essential  
RUN apt-get install -y libsdl2-dev  
RUN apt-get install -y libsdl2-ttf-dev  
RUN apt-get install -y libfontconfig-dev  
RUN apt-get install -y qt5-default  
RUN apt-get install -y wget  
RUN apt-get install -y libqt4-*  
RUN apt-get install -y libsdl-ttf2.0-dev  
RUN apt-get install -y libgtk2.0-dev  
RUN apt-get install -y libgconf2-dev  
RUN apt-get install -y subversion  
  
ENV VER 0164  
  
VOLUME /workspace  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["build"]  

