# tinyMediaManager  
FROM hurricane/dockergui:x11rdp1.3  
MAINTAINER Carlos Hernandez <carlos@techbyte.ca>  
  
#########################################  
## ENVIRONMENTAL CONFIG ##  
#########################################  
# Set correct environment variables  
ENV LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
ENV APP_NAME tinyMediaManager  
  
#########################################  
## Use baseimage-docker's init system ##  
#########################################  
CMD ["/sbin/my_init"]  
  
#########################################  
## RUN INSTALL SCRIPT ##  
#########################################  
COPY ./files/ /tmp/  
#########################################  
## INSTALL LIBMEDIAINFO ##  
#########################################  
RUN apt-get update && apt-get install -y libmediainfo0  
RUN apt-get install python-xdg  
RUN apt-get install -f  
  
#########################################  
## INSTALL DIRECTLY FROM RELEASE PAGE ##  
#########################################  
RUN mkdir /tinyMediaManager && chmod 775 /tinyMediaManager  
RUN tar -zxvf /tmp/tmm.tar.gz -C /tinyMediaManager  
RUN chmod +x /tmp/install/tmm_install.sh && sleep 1 &&
/tmp/install/tmm_install.sh && rm -r /tmp/install  
  
#########################################  
## EXPORTS AND VOLUMES ##  
#########################################  
VOLUME ["/config"]  
VOLUME ["/mnt"]  
EXPOSE 3389 8080  

