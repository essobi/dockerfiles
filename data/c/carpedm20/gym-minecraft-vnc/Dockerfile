FROM ubuntu:16.04  
ENV VNC_PASS mine  
ENV MALMO_PATH /root/Malmo/  
ENV MALMO_XSD_PATH $MALMO_PATH/Schemas  
  
# install Malmo dependencies  
RUN apt-get update && apt-get install -y \  
libboost-all-dev \  
libpython2.7 \  
openjdk-8-jdk \  
lua5.1 \  
libxerces-c3.1 \  
liblua5.1-0-dev \  
libav-tools \  
python-tk \  
python-imaging-tk \  
wget \  
unzip \  
xvfb \  
x11vnc  
  
RUN update-ca-certificates -f  
  
# download and unpack Malmo  
WORKDIR /root  
RUN wget
https://github.com/Microsoft/malmo/releases/download/0.18.0/Malmo-0.18.0-Linux-
Ubuntu-16.04-64bit.zip  
RUN unzip Malmo-0.18.0-Linux-Ubuntu-16.04-64bit.zip  
RUN rm Malmo-0.18.0-Linux-Ubuntu-16.04-64bit.zip  
RUN mv Malmo-0.18.0-Linux-Ubuntu-16.04-64bit Malmo  
  
# precompile stuff  
RUN mkdir ~/.gradle && echo 'org.gradle.daemon=true\n' >
~/.gradle/gradle.properties  
WORKDIR $MALMO_PATH/Minecraft  
RUN ./gradlew setupDecompWorkspace  
RUN ./gradlew build  
  
# clean up  
RUN apt-get clean  
RUN rm -rf /tmp/* /tmp/.[!.]* /tmp/..?* /var/lib/apt/lists/*  
  
# unlimited framerate settings  
COPY options.txt /root/Malmo/Minecraft/run  
  
# run Malmo  
EXPOSE 5900 10000  
COPY run.sh /root/  
  
ENTRYPOINT ["/root/run.sh"]  

