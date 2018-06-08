FROM fabric8/builder-clients:0.9  
ENV FUNKTION_VERSION 1.0.13  
RUN curl -O --retry 999 --retry-max-time 0 -sSL
https://github.com/funktionio/funktion/releases/download/v$FUNKTION_VERSION/funktion-
linux-amd64 && \  
chmod +x funktion-linux-amd64 && \  
mv funktion-linux-amd64 /usr/bin/funktion  
  

