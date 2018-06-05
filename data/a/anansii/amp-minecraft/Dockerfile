FROM debian:stretch  
  
ENV USER=AMP UID=1000 GID=1000 MODULE=Minecraft
EXTRAS="+MinecraftModule.Minecraft.PortNumber 25565"  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
lib32gcc1 \  
coreutils \  
screen \  
tmux \  
socat \  
unzip \  
zip \  
git \  
wget \  
libsqlite3-dev \  
daemontools \  
openjdk-8-jdk-headless \  
&& rm -rf \  
/tmp/* \  
/var/tmp/* \  
/var/lib/apt/lists/*  
  
RUN \  
groupadd --gid "${GID}" "${USER}" && \  
useradd \  
\--uid ${UID} \  
\--gid ${GID} \  
\--create-home \  
\--shell /bin/bash \  
${USER} && \  
mkdir /home/"${USER}"/"${USER}" && \  
cd /home/"${USER}"/"${USER}" && \  
wget http://cubecoders.com/Downloads/ampinstmgr.zip && \  
unzip ampinstmgr.zip && \  
rm -fi \--interactive=never ampinstmgr.zip  
  
# Define working directory.  
WORKDIR /home/"${USER}"/"${USER}"  
  
COPY start.sh /home/"${USER}"/"${USER}"/  
  
RUN \  
mkdir /ampdata && \  
chown "${USER}":"${USER}" /ampdata && \  
chown "${USER}":"${USER}" ./start.sh && \  
chmod +x ./start.sh  
  
VOLUME ["/ampdata"]  
  
USER "${USER}"  
# Define default command.  
ENTRYPOINT ["./start.sh"]  
  
RUN ln -s /ampdata /home/"${USER}"/.ampdata  
  
# Expose ports.  
EXPOSE 8080 25565  

