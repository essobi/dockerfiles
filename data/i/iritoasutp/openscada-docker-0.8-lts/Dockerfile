FROM ubuntu:16.04  
RUN apt-get update -y  
RUN apt-get install software-properties-common wget -y  
RUN apt-add-repository "deb http://ftp.oscada.org/OpenSCADA/0.8.0/Ubuntu/16.04
./"  
RUN wget -q -O- http://ftp.oscada.org/Misc/pkgSignKey | apt-key add -  
RUN apt-get update -y  
RUN apt-get install openscada -y  
RUN apt-get install openscada-libdb-main  
RUN apt-get install openscada-libdb-vca  
  
EXPOSE 10002  
CMD ["/usr/bin/openscada_start", "--noX11"]  

