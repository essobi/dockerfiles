FROM gorzechowski/clang:xenial  
  
RUN add-apt-repository -y ppa:beineri/opt-qt562-xenial  
  
RUN apt-get update && apt-get -y install \  
qt56base \  
qt56websockets  
  
RUN echo "source /opt/qt56/bin/qt56-env.sh" >> /etc/profile  
RUN echo "export QMAKESPEC=/opt/qt56/mkspecs/linux-clang" >> /etc/profile  

