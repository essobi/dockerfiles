FROM jsurf/rpi-raspbian:latest  
  
RUN [ "cross-build-start" ]  
  
ENV TZ Europe/Berlin  
  
RUN apt-get update \  
&& apt-get install -y curl ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -s
https://packagecloud.io/install/repositories/jsurf/raspbian/script.deb.sh |
bash \  
&& apt-get update \  
&& apt-get install hmcfgusb \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 1000  
  
CMD ["hmland","-p","1000" ]  
  
RUN [ "cross-build-end" ]  

