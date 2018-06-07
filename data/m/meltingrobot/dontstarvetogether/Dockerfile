# Version 0.0.1  
FROM centos:latest  
MAINTAINER Roy P "meltingrobot@gmail.com"  
RUN yum -y update  
RUN yum -y install libcurl.i686 libgcc.i686 glibc.i686 tar wget  
RUN mkdir /usr/local/dontstarvetogether  
RUN mkdir /usr/local/steamcmd  
RUN wget -P /usr/local/steamcmd
http://media.steampowered.com/installer/steamcmd_linux.tar.gz  
RUN tar -C /usr/local/steamcmd -xvzf /usr/local/steamcmd/steamcmd_linux.tar.gz  
RUN ln -s /usr/lib/libcurl.so.4 /usr/lib/libcurl-gnutls.so.4  
CMD [ "/bin/bash", "-c", "/usr/local/steamcmd/steamcmd.sh +login anonymous
+force_install_dir /usr/local/dontstarvetogether +app_update 343050 -validate
+quit; cd /usr/local/dontstarvetogether/bin ;
./dontstarve_dedicated_server_nullrenderer" ]  
VOLUME /root/.klei  
VOLUME /usr/local/dontstarvetogether  
EXPOSE 10999/udp  

