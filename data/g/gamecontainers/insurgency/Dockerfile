FROM crosbymichael/steamcmd  
  
WORKDIR /home/daemon/steamcmd/insurgency/  
ADD server.cfg /home/daemon/steamcmd/insurgency/insurgency/cfg/  
  
ENTRYPOINT ["./srcds_linux", "-game", "insurgency", "-console"]  

