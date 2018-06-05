FROM debian:stretch  
RUN apt-get update \  
&& apt-get install -y curl mosquitto-clients \  
&& curl -L https://github.com/Motion-
Project/motion/releases/download/release-4.1.1/stretch_motion_4.1.1-1_amd64.deb
-o /tmp/motion.deb \  
&& dpkg -i /tmp/motion.deb || true \  
&& apt-get install -fy \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm /tmp/motion.deb  
  
EXPOSE 8080 8081  
CMD ["motion", "-n"]  

