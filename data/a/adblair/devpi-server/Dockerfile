FROM ioft/armhf-ubuntu:14.04  
MAINTAINER Arthur Blair <adblair@gmail.com>  
  
RUN apt-get update && apt-get install python3-pip && apt-get clean  
  
RUN pip install devpi-server==2.3.1 devpi-web==2.4.1  
  
EXPOSE 3141  
VOLUME /srv/devpi-server  
  
CMD ["devpi-server", "--host", "0.0.0.0", "--port", "3141", "--serverdir",
"/srv/devpi-server"]  

