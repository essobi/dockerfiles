# ==================  
# Steam Dockerfile  
# PrivateHeberg©  
# ==================  
FROM debian:8  
MAINTAINER privateHeberg  
  
# ==== Variables ==== #  
ENV GAME_ID=""  
ENV MAX_PLAYER=10  
ENV API_KEY=""  
ENV GAME_NAME=""  
ENV GAME_PARAMS=""  
ENV GAME_PORT=27015  
# =================== #  
# ==== Paquets ==== #  
RUN apt-get update &&\  
apt-get install -y curl lib32gcc1 lsof git &&\  
apt-get install lib32stdc++6  
# ================= #  
# ==== Steam user ==== #  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
steam  
RUN usermod -a -G sudo steam  
# ==================== #  
# ==== Scripts ==== #  
COPY run.sh /home/steam/run.sh  
RUN touch /root/.bash_profile  
RUN chmod 777 /home/steam/run.sh  
RUN mkdir /data  
RUN chown steam -R /data && chmod 755 -R /data  
# ================= #  
# ==== SteamCMD ==== #  
RUN mkdir /home/steam/steamcmd &&\  
cd /home/steam/steamcmd &&\  
curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz  
# ================== #  
# ==== Port ==== #  
EXPOSE ${GAME_PORT}  
EXPOSE ${GAME_PORT}/udp  
# ================== #  
# ==== Volumes ==== #  
VOLUME /data  
WORKDIR /data  
# ================= #  
ENTRYPOINT ["/home/steam/run.sh"]

