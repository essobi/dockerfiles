FROM ubuntu:14.04  
RUN apt-get clean && apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install gcc  
RUN apt-get -y install build-essential  
RUN apt-get -y install smlnj  
RUN apt-get -y install rlwrap  
RUN echo "alias sml='rlwrap sml -Ccontrol.poly-eq-warn=false'" >> ~/.bashrc  
  
RUN mkdir /opt/smlnj  
VOLUME /opt/smlnj  
WORKDIR /opt/smlnj

