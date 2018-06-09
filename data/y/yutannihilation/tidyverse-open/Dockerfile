FROM rocker/tidyverse:latest  
  
RUN wget -P /usr/local/bin/
https://github.com/yutannihilation/rstudioexposer/releases/download/v0.0.1/rstudioexposer
\  
&& chmod +x /usr/local/bin/rstudioexposer \  
&& mkdir -p /etc/services.d/rstudioexposer \  
&& echo '#!/bin/bash \  
\n exec /usr/local/bin/rstudioexposer' \  
> /etc/services.d/rstudioexposer/run  
  
EXPOSE 80 8787

