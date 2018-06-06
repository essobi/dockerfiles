FROM ubuntu:16.04  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y chromium-browser chromium-chromedriver \  
&& apt-get install -y xvfb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix && chown root
/tmp/.X11-unix/  
  
ADD xvfb.sh /bin/  
RUN useradd -ms /bin/sh user  
USER user  
USER root  
#RUN apt update && apt install -y strace  
WORKDIR /home/user  
USER user  
ENV DISPLAY ":10.0"  
CMD ["xvfb.sh","DISPLAY","start"]  
  

