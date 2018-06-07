FROM ubuntu:14.04  
MAINTAINER improvshark <improvshark@gmail.com>  
  
# Install base packages  
RUN apt-get -qq update  
RUN apt-get -qq -y upgrade  
RUN apt-get -qq update  
  
# install dependancy  
RUN apt-get -y install curl lib32gcc1  
  
# install steamcmd  
RUN mkdir -p /opt/steamcmd &&\  
cd /opt/steamcmd &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
# install dont starve together  
RUN mkdir -p /opt/dontStarveTogether  
RUN /opt/steamcmd/steamcmd.sh \  
+login anonymous \  
+force_install_dir /opt/dontStarveTogether \  
+app_update 343050 validate \  
+quit  
  
#fix dependancy problems  
RUN dpkg --add-architecture i386  
RUN apt-get -qq update && apt-get -qq -y install libcurl4-gnutls-dev:i386 vim  
RUN ln -s /opt/steamcmd/linux32/libstdc++.so.6
/opt/dontStarveTogether/bin/lib32/  
  
# create save dir and link  
RUN mkdir -p /opt/save/  
RUN mkdir -p /root/.klei/  
RUN ln -s /opt/save /root/.klei/DoNotStarveTogether  
  
#add user  
#RUN useradd -ms /bin/bash steam  
#RUN chown steam:steam -R /opt  
#USER steam  
# create a volume for modifications of files  
VOLUME /opt/  
  
# Expose ports  
EXPOSE 10999/udp  
  
# Define default command.  
WORKDIR /opt/dontStarveTogether/bin  
  
# install mod files  
RUN ./dontstarve_dedicated_server_nullrenderer -only_update_server_mods  
#CMD ["/bin/bash"]  
CMD ["./dontstarve_dedicated_server_nullrenderer","-shard","Master"]  

