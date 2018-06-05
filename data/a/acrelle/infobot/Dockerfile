FROM debian:latest  
LABEL maintainer="anthony@relle.co.uk"  
  
ADD discord.patch annoying.patch schedulers.patch /tmp/  
  
ARG PUID=1001  
ARG PGID=100  
RUN groupadd -o -g ${PGID} -r infobot && useradd --no-log-init -r -o -u
${PUID} -g infobot -m infobot  
  
# install build packages  
RUN apt-get update && \  
apt-get install -y libnet-irc-perl libwww-search-perl libwww-perl libhtml-
parser-perl libxml-feed-perl libsqlite0 libdbd-sqlite3-perl git patch && \  
cd /home/infobot/ && git clone https://github.com/acrelle/infobot.git infobot-
code && \  
cd /home/infobot/infobot-code/src/IRC && cat /tmp/discord.patch | patch && \  
cd /home/infobot/infobot-code/src/Factoids && cat /tmp/annoying.patch | patch
&& \  
cd /home/infobot/infobot-code/src/IRC && cat /tmp/schedulers.patch | patch &&
\  
apt-get remove -y git patch && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
chown -R infobot:infobot /home/infobot/infobot-code  
  
# ports and volumes  
USER infobot  
VOLUME ["/home/infobot/infobot-code/files", "/home/infobot/infobot-code/log" ]  
WORKDIR /home/infobot/infobot-code  
CMD ["/home/infobot/infobot-code/infobot"]  

