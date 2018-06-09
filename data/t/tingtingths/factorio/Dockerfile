# Dockerfile for latest factorio headless server  
FROM ubuntu:17.10  
ENV RCON_PASSWD defaultrconpassword  
  
RUN mkdir -p /app \  
/app/data  
  
WORKDIR /app  
RUN apt-get update && apt-get -y install wget tar xz-utils  
  
# Prepare factorio headless binary  
RUN wget https://www.factorio.com/get-download/stable/headless/linux64 -O
tmp.tar \  
&& tar xvf tmp.tar && rm tmp.tar  
  
# Install fac  
RUN apt-get update && apt-get -y install python3 python3-pip  
RUN pip3 install fac-cli  
RUN ln -s /app/data/mods /app/factorio/mods  
RUN mkdir -p ~/.config/fac/  
RUN echo ' \  
[paths] \  
data-path = /app/factorio/data \  
write-path = /app/factorio \  
' > ~/.config/fac/config.ini  
  
EXPOSE 34197/udp 27015  
CMD ["/app/factorio/bin/x64/factorio", "--start-server", "/app/data/save.zip",
"--server-settings", "/app/data/server-settings.json", "--rcon-port", "27015",
"--rcon-password", "${RCON_PASSWD}", "--mod-directory", "/app/data/mods"]  

