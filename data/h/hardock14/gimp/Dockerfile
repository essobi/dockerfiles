# New Image based on digikam-17.04 image  
FROM hardock14/docker-headless-ubuntu-vnc-container:17.04  
MAINTAINER Harald Graf  
ENV REFRESHED_AT 2017-09-12  
### Install additional programs - gimp  
RUN apt-get update && apt-get install -y \  
gimp \  
gtk3-engines-breeze \  
breeze-icon-theme \  
breeze-cursor-theme \  
fonts-noto \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5901  
EXPOSE 6901  
ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]  
CMD ["--tail-log"]  

