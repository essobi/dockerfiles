FROM python:3.5.2  
ARG googler_url=https://raw.githubusercontent.com/jarun/googler/master/googler  
ARG googler_exec=/usr/local/bin/googler  
  
RUN wget $googler_url -qO $googler_exec \  
&& chmod +x $googler_exec  
  
ENTRYPOINT ["googler"]  

