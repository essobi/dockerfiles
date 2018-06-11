FROM ubuntu:14.04  
ENV DIR /armbian  
ENV TERM xterm  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys E083A3782A194991 && \  
echo "deb http://repo.aptly.info/ squeeze main" >
/etc/apt/sources.list.d/aptly.list  
RUN apt-get update && \  
apt-get install -y git aptly  
  
RUN mkdir $DIR  
RUN cd $DIR && git clone https://github.com/igorpecovnik/lib.git --depth 1  
  
RUN cp $DIR/lib/compile.sh $DIR/.  
RUN chmod +x $DIR/compile.sh  
VOLUME ["$DIR"/compiled]  
WORKDIR "$DIR"  
  
RUN ./compile.sh BRANCH=next BOARD=lamobo-r1 KERNEL_ONLY=yes
KERNEL_CONFIGURE=no BUILD_DESKTOP=no PROGRESS_DISPLAY=plain RELEASE=jessie  
  
#ENTRYPOINT ["./compile.sh"]  

