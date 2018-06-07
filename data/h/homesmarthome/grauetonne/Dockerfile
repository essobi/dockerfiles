FROM resin/rpi-raspbian:jessie  
  
RUN apt-get update && apt-get install -y \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY grauetonne.sh /grauetonne.sh  
RUN chmod a+x /grauetonne.sh  
  
CMD ["/grauetonne.sh"]  

