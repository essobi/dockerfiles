# Run Rapid Photo Downloader in a container on windows  
#  
# vcxsrv  
# docker run -it -e DISPLAY=<server>:0.0 -v <source>:/data/source -v
<target>:/data/target/ -v
<dir>\RapidPhotoDownloaderConfig\local\:/home/rpd/.local/share/ -v
<dir>\RapidPhotoDownloaderConfig\home\:/home/rpd/ randyklein99/rapid-photo-
downloader  
  
FROM ubuntu:18.04  
  
## from https://hub.docker.com/r/library/ubuntu/  
#RUN apt-get update && apt-get install -y locales && rm -rf
/var/lib/apt/lists/* \  
# && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
#ENV LANG en_US.utf8  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales tzdata  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
  
  
  
RUN apt-get update && apt-get install -y \  
rapid-photo-downloader  
  
# needs home directory with -m  
RUN groupadd -r rpd && useradd -m -g rpd rpd  
  
#VOLUME [ "/data/source/" ]  
#VOLUME [ "/data/target/" ]  
  
# create a volume to persist configuration  
# location will change with 0.9 version in ubuntu 18.04  
#VOLUME [ "/home/rpd/" ]  
#VOLUME [ "/home/rpd/.local/share/" ]  
  
USER rpd  
WORKDIR /home/rpd  
  
CMD [ "/usr/bin/rapid-photo-downloader" ]  
#CMD [ "" ]  
  
# Still getting following error:  
#Traceback (most recent call last):  
# File "/usr/bin/rapid-photo-downloader", line 6, in <module>  
# from pkg_resources import load_entry_point  
#ModuleNotFoundError: No module named 'pkg_resources'  

