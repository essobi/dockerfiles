# ==================  
# Unturned Dockerfile  
# PrivateHeberg©  
# ==================  
FROM debian:8  
MAINTAINER privateHeberg  
  
# ==== Variables ==== #  
ENV STEAM_USER anonymous  
ENV STEAM_PASSWORD ""  
ENV INSTANCE_ID=""  
ENV INSTANCE_PORT=27015  
ENV SLOTS=16  
# =================== #  
# ==== Paquets ==== #  
RUN apt-get update &&\  
apt-get -y install curl unzip wget  
RUN dpkg --add-architecture i386  
RUN apt-get update &&\  
apt-get -y install lib32stdc++6 &&\  
apt-get -y install mono-runtime libmono2.0-cil &&\  
apt-get -y install libc6 libgl1-mesa-glx libxcursor1 libxrandr2 &&\  
apt-get -y install libc6-dev-i386 libgcc-4.8-dev  
# ================= #  
# ==== Scripts ==== #  
COPY run.sh /home/unturned/run.sh  
RUN touch /root/.bash_profile  
RUN chmod 777 /home/unturned/run.sh  
RUN mkdir /data  
# ================= #  
# ==== SteamCMD ==== #  
RUN mkdir /home/unturned/steamcmd &&\  
cd /home/unturned/steamcmd &&\  
curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
# ================== #  
# ==== Volumes ==== #  
VOLUME /data  
WORKDIR /data  
# ================= #  
ENTRYPOINT ["/home/unturned/run.sh"]

