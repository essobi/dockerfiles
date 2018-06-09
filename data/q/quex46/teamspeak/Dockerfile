FROM debian  
  
ENV ver 3.0.11.4  
ADD http://dl.4players.de/ts/releases/${ver}/teamspeak3-server_linux-
amd64-${ver}.tar.gz ./  
COPY ./entrypoint.sh ./opt/teamspeak/  
  
RUN tar -zxf teamspeak3-server_linux-amd64-${ver}.tar.gz && \  
mv teamspeak3-server_linux-amd64/* /opt/teamspeak/ && \  
rm teamspeak3-server_linux-amd64-${ver}.tar.gz  
  
VOLUME ["/opt/teamspeak/data"]  
  
ENTRYPOINT ["/opt/teamspeak/entrypoint.sh"]  
  
EXPOSE 9987/udp 30033 10011

