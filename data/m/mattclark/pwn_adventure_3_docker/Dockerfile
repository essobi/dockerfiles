FROM ubuntu:16.04  
EXPOSE 5432  
RUN apt update && apt install -y wget postgresql git unzip&& mkdir -p
/opt/pwn3  
  
WORKDIR /opt/pwn3  
  
RUN useradd -ms /bin/bash pwn3  
  
RUN wget http://www.pwnadventure.com/PwnAdventure3Server.tar.gz && tar -zxf
PwnAdventure3Server.tar.gz && wget
http://www.pwnadventure.com/PwnAdventure3_Launcher_Linux.zip && unzip
PwnAdventure3_Launcher_Linux.zip && mv PwnAdventure3Servers/* . && rm *.gz &&
rm *zip && rm -R PwnAdventure3Servers && cp MasterServer/initdb.sql initdb.sql
&& chown pwn3 initdb.sql  
  

