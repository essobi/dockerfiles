FROM ubuntu:latest  
RUN dpkg --add-architecture i386 && apt-get update && apt-get upgrade -y &&
apt-get autoremove -y && apt-get autoclean -y  
RUN apt-get install -y screen wget unzip rsync lib32stdc++6 mono-runtime mono-
reference-assemblies-2.0 libc6:i386 libgl1-mesa-glx:i386 libxcursor1:i386
libxrandr2:i386 libc6-dev-i386 libgcc-4.8-dev:i386  
RUN wget
https://raw.githubusercontent.com/jpenton/Rocket.Unturned/master/Rocket.Unturned/Scripts/Linux/rocket.sh
-P /root/Scripts/  
RUN wget
https://cdn.rawgit.com/jpenton/Rocket.Unturned/master/Rocket.Unturned/Scripts/Linux/start.sh
https://cdn.rawgit.com/jpenton/Rocket.Unturned/master/Rocket.Unturned/Scripts/Linux/update.sh
-P /root/Scripts/  
RUN chmod +x /root/Scripts/*  
RUN sed -i -e 's/\r$//' /root/Scripts/update.sh  
RUN /root/Scripts/update.sh computerunturned1 pokemonjon  
RUN sed -i -e 's/\r$//' /root/Scripts/rocket.sh  
RUN /root/Scripts/rocket.sh  
RUN sed -i -e 's/\r$//' /root/Scripts/start.sh  

