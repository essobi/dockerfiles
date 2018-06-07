# Counter-Strike Global Offensive Dedicated Server  
#  
# Version 1.0.0  
FROM tingvarsson/steamcmd:latest  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
ENV CSGO_DIR $HOME/csgo  
  
ADD start.sh $HOME/start.sh  
  
WORKDIR $HOME  
  
EXPOSE 27015  
CMD ["./start.sh"]

