FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y wget nano xz-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m -d /opt/factorio -s /bin/bash factorio \  
&& chown -R factorio.factorio /opt/factorio  
USER factorio  
  
ENV HOME /opt/factorio  
ENV SAVEFILE /opt/factorio/saves/factorio_save.zip  
ENV FACTORIO_SERVER_GAME Cult of the Factorio  
ENV FACTORIO_SERVER_GAME_PASSWORD cultofthefactorio  
ENV FACTORIO_SERVER_PORT 34197  
WORKDIR /opt/factorio  
  
RUN wget -q -O - https://www.factorio.com/download-headless/stable | grep -o
-m1 "/get-download/.*/headless/linux64" | awk '{print "--no-check-certificate
https://www.factorio.com"$1" -O /tmp/factorio.tar.xz"}' | xargs wget \  
&& tar -xf /tmp/factorio.tar.xz -C /opt \  
&& rm -rf /tmp/factorio.tar.xz  
  
ADD init.sh /opt/factorio/  
ADD server-settings.example.json /opt/factorio/data/  
  
EXPOSE 34197/udp  
CMD ["./init.sh"]  

