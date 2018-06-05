FROM ubuntu:latest  
  
# Dependencies  
RUN apt-get update  
RUN apt-get -y install git-core gcc make cmake qt5-default g++ libqt5svg5-dev
pkg-config  
  
# Get cutter  
WORKDIR /opt  
RUN git clone https://github.com/radareorg/cutter cutter  
  
# Build radare2  
WORKDIR /opt/cutter  
RUN git submodule init radare2 && git submodule update radare2  
RUN cd radare2 && ./sys/install.sh  
  
# Build cutter  
RUN mkdir build  
WORKDIR /opt/cutter/build  
RUN cmake ../src  
RUN make  
  
# Add r2 user  
RUN useradd r2  
  
WORKDIR /home/r2  
RUN mkdir /var/sharedFolder  
RUN mkdir -p /home/r2/.config/radare2  
RUN touch /home/r2/.radare2rc  
  
RUN chown -R r2:r2 /var/sharedFolder  
RUN chown -R r2:r2 /home/r2/  
USER r2  
  
ENTRYPOINT ["/bin/bash", "-c", "/opt/cutter/build/cutter"]  

