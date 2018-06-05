FROM mono:latest  
MAINTAINER David Pedersen <limero@me.com>  
  
RUN curl -O -L $(curl -s
https://api.github.com/repos/JustArchi/ArchiSteamFarm/releases/latest | grep
'browser_' | cut -d\" -f4 | grep '.exe')  
  
CMD ["mono", "ASF.exe"]  

