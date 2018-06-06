FROM ubuntu:latest  
  
RUN apt-get clean && apt-get update && apt-get install -y locales  
  
# enable utf-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV TERM xterm  
  
ADD install.sh /tmp/install.sh  
RUN sh -e /tmp/install.sh  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +rx /tini  
  
# install intermec drivers  
ADD drivers ./drivers  
RUN cd ./drivers && tar -zxvf cupsdriver-1.2-56.tar.gz && cd cupsdriver-1.2-56
&& ./build.sh  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["/usr/sbin/cupsd", "-f"]  

