FROM ubuntu:16.04  
MAINTAINER sascha.herrmann.consulting@gmail.com  
  
# Inspired by suchja/wine, monokrome/wine and ColinHuang/docker-ubuntu-wine  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN useradd -m -d /home/gamsuser -U gamsuser  
RUN dpkg --add-architecture i386  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common curl  
#RUN apt-get install -y software-properties-common curl xvfb  
RUN apt-get install -y -f wine  
RUN apt-get install -y winetricks  
RUN sudo apt-get install -y software-properties-common  
RUN sudo add-apt-repository multiverse  
RUN sudo add-apt-repository universe  
RUN apt-get update -y  
RUN apt-get install -y dosbox:any winbind  
RUN apt-get install -y fonts-droid-fallback ttf-mscorefonts-installer wine-
gecko2.21 wine-mono0.0.8 wine-gecko2.21:i386 wine-mono0.0.8:i386  
  
#RUN apt-get purge -y software-properties-common  
#RUN apt-get autoclean -y  
#RUN apt-get autoremove -y  
#RUN rm -rf /var/lib/apt/lists/*  
# Download appropriate GAMS-Version  
RUN curl -SL
https://d37drm4t2jghv5.cloudfront.net/distributions/24.5.6/windows/windows_x86_32.exe
-o /home/gamsuser/windows_x86_32.exe  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
USER gamsuser  
WORKDIR /home/gamsuser  
ENV WINEPREFIX /home/gamsuser/.wine  
ENV WINEARCH win32  
# Deactivated GAMS-Installation during image creation for the moment  
#RUN xvfb-run -a wine windows_x86_32.exe /SP- /SILENT && touch
/home/gamsuser/.gams_is_installed  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

