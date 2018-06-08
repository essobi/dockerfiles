FROM jamesandariese/xpra-base  
  
RUN apt-get update && \  
apt-get install -y pidgin && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -sf /root/.purple /purple  
  
VOLUME ["/purple"]  
  
# don't forget to create your /password file  
CMD ["--start-child=pidgin"]  

