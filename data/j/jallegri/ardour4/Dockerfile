FROM jallegri/ubuntustudio-audio-base  
  
RUN \  
apt-get update && \  
apt-get install -y ardour && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["ardour4"]  

