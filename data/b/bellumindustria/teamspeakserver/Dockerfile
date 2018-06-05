#  
# Dockerfile for Teamspeak server  
#  
# @see https://github.com/bellumindustria/docker-csgoserver  
#  
FROM bellumindustria/linuxgsmserver:release-1.0.1  
MAINTAINER Antoine Benevaut <antoine@bellum-industria.fr>  
  
# Teamspeak 3/MySQL database variables  
ARG TS3_MACHINE_ID=1  
ARG TS3_LICENSEPATH=""  
ARG TS3_VOICE_PORT=9987  
ARG TS3_VOICE_IP="0.0.0.0, ::"  
ARG TS3_QUERY_PORT=10011  
ARG TS3_QUERY_IP="0.0.0.0, ::"  
ARG TS3_FILE_TRANSFERS_PORT=30033  
ARG TS3_FILE_TRANSFERS_IP="0.0.0.0, ::"  
ARG TS3_QUERY_IP_WITHELIST="query_ip_whitelist.txt"  
ARG TS3_QUERY_IP_BLACKLIST="query_ip_blacklist.txt"  
ARG TS3_DB_PLUGIN="ts3db_mariadb"  
ARG TS3_DB_PLUGIN_PARAMETER="ts3db_mariadb.ini"  
ARG TS3_DB_SQL_PATH="sql/"  
ARG TS3_DB_SQL_CREATE_PATH="create_mariadb/"  
ARG TS3_DB_CONNECTIONS=10  
ARG TS3_LOG_PATH=logs  
ARG TS3_LOG_QUERY_COMMANDS=0  
ARG TS3_DB_CLIENT_KEEP_DAYS=30  
ARG TS3_LOG_APPEND=0  
ARG TS3_QUERY_SKIP_BRUTE_FORCE_CHECK=0  
ARG TS3_UPDATE_ON_START=on  
ARG TS3_EMAIL_ALERT=on  
ARG TS3_EMAIL="contact@bellum-industria.fr"  
ARG TS3_EMAIL_FROM=""  
ARG TS3_PUSHBULLET_ALERT=""  
ARG TS3_PUSHBULLET_TOKEN=""  
ARG TS3_PUSHBULLET_CHANNEL_TAG=""  
ARG TS3_MYSQL_HOST=mysql  
ARG TS3_MYSQL_PORT=3306  
ARG TS3_MYSQL_DB=default  
ARG TS3_MYSQL_USER=default  
ARG TS3_MYSQL_PASS=secret  
ARG TS3_MYSQL_SOCKET=""  
ENV TS3_MACHINE_ID ${TS3_MACHINE_ID}  
ENV TS3_LICENSEPATH ${TS3_LICENSEPATH}  
ENV TS3_VOICE_PORT ${TS3_VOICE_PORT}  
ENV TS3_VOICE_IP ${TS3_VOICE_IP}  
ENV TS3_QUERY_PORT ${TS3_QUERY_PORT}  
ENV TS3_QUERY_IP ${TS3_QUERY_IP}  
ENV TS3_FILE_TRANSFERS_PORT ${TS3_FILE_TRANSFERS_PORT}  
ENV TS3_FILE_TRANSFERS_IP ${TS3_FILE_TRANSFERS_IP}  
ENV TS3_QUERY_IP_WITHELIST ${TS3_QUERY_IP_WITHELIST}  
ENV TS3_QUERY_IP_BLACKLIST ${TS3_QUERY_IP_BLACKLIST}  
ENV TS3_DB_PLUGIN ${TS3_DB_PLUGIN}  
ENV TS3_DB_PLUGIN_PARAMETER ${TS3_DB_PLUGIN_PARAMETER}  
ENV TS3_DB_SQL_PATH ${TS3_DB_SQL_PATH}  
ENV TS3_DB_SQL_CREATE_PATH ${TS3_DB_SQL_CREATE_PATH}  
ENV TS3_DB_CONNECTIONS ${TS3_DB_CONNECTIONS}  
ENV TS3_LOG_PATH ${TS3_LOG_PATH}  
ENV TS3_LOG_QUERY_COMMANDS ${TS3_LOG_QUERY_COMMANDS}  
ENV TS3_DB_CLIENT_KEEP_DAYS ${TS3_DB_CLIENT_KEEP_DAYS}  
ENV TS3_LOG_APPEND ${TS3_LOG_APPEND}  
ENV TS3_QUERY_SKIP_BRUTE_FORCE_CHECK ${TS3_QUERY_SKIP_BRUTE_FORCE_CHECK}  
ENV TS3_UPDATE_ON_START ${TS3_UPDATE_ON_START}  
ENV TS3_EMAIL_ALERT ${TS3_EMAIL_ALERT}  
ENV TS3_EMAIL ${TS3_EMAIL}  
ENV TS3_EMAIL_FROM ${TS3_EMAIL_FROM}  
ENV TS3_PUSHBULLET_ALERT ${TS3_PUSHBULLET_ALERT}  
ENV TS3_PUSHBULLET_TOKEN ${TS3_PUSHBULLET_TOKEN}  
ENV TS3_PUSHBULLET_CHANNEL_TAG ${TS3_PUSHBULLET_CHANNEL_TAG}  
ENV TS3_MYSQL_HOST ${TS3_MYSQL_HOST}  
ENV TS3_MYSQL_PORT ${TS3_MYSQL_PORT}  
ENV TS3_MYSQL_DB ${TS3_MYSQL_DB}  
ENV TS3_MYSQL_USER ${TS3_MYSQL_USER}  
ENV TS3_MYSQL_PASS ${TS3_MYSQL_PASS}  
ENV TS3_MYSQL_SOCKET ${TS3_MYSQL_SOCKET}  
  
# Exposing Teamspeak3 ports  
EXPOSE $TS3_VOICE_PORT/udp  
EXPOSE $TS3_QUERY_PORT  
EXPOSE $TS3_FILE_TRANSFERS_PORT  
  
# Create user to run as  
# script refuses to run in root, create user  
RUN groupadd -r ts3server && \  
useradd -rm -g ts3server ts3server && \  
adduser ts3server sudo && \  
echo "ts3server ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ADD ts3db_mariadb.ini /home/ts3server/serverfiles/ts3db_mariadb.ini  
  
RUN chown -R ts3server:ts3server /home/ts3server  
  
USER ts3server  
WORKDIR /home/ts3server  
  
# Download Teamspeak Server Manager Script  
RUN wget
https://raw.githubusercontent.com/GameServerManagers/LinuxGSM/170501/TeamSpeak3/ts3server
&& \  
chmod +x ts3server  
  
# Edit Server Script to hold Docker Environmental Varables  
RUN sed -i '/emailalert=/s/"\\([^"]*\\)"/"$TS3_EMAIL_ALERT"/' ts3server && \  
sed -i '/email=/s/"\\([^"]*\\)"/"$TS3_EMAIL"/' ts3server && \  
sed -i '/emailfrom=/s/"\\([^"]*\\)"/"$TS3_EMAIL_FROM"/' ts3server && \  
sed -i '/pushbulletalert=/s/"\\([^"]*\\)"/"$TS3_PUSHBULLET_ALERT"/' ts3server
&& \  
sed -i '/pushbullettoken=/s/"\\([^"]*\\)"/"$TS3_PUSHBULLET_TOKEN"/' ts3server
&& \  
sed -i '/channeltag=/s/"\\([^"]*\\)"/"$TS3_PUSHBULLET_CHANNEL_TAG"/' ts3server
&& \  
sed -i '/updateonstart=/s/"\\([^"]*\\)"/"$TS3_UPDATE_ON_START"/' ts3server  
  
# Run Install Script  
RUN ./ts3server auto-install  
RUN mkdir -p /home/ts3server/serverfiles && \  
mkdir -p /home/ts3server/backups && \  
mkdir -p /home/ts3server/log && \  
chown -R ts3server:ts3server /home/ts3server  
  
# Volumes  
VOLUME ["/home/ts3server/serverfiles/files", "/home/ts3server/log",
"/home/ts3server/backups"]  
  
# Edit Server Script to hold Docker Environmental Varables  
RUN echo "machine_id=${TS3_MACHINE_ID}" > serverfiles/ts3-server.ini && \  
echo "default_voice_port=${TS3_VOICE_PORT}" >> serverfiles/ts3-server.ini && \  
echo "voice_ip=${TS3_VOICE_IP}" >> serverfiles/ts3-server.ini && \  
echo "licensepath=${TS3_LICENSEPATH}" >> serverfiles/ts3-server.ini && \  
echo "filetransfer_port=${TS3_FILE_TRANSFERS_PORT}" >>
serverfiles/ts3-server.ini && \  
echo "filetransfer_ip=${TS3_FILE_TRANSFERS_IP}" >> serverfiles/ts3-server.ini
&& \  
echo "query_port=${TS3_QUERY_PORT}" >> serverfiles/ts3-server.ini && \  
echo "query_ip=${TS3_QUERY_IP}" >> serverfiles/ts3-server.ini && \  
echo "query_ip_whitelist=${TS3_QUERY_IP_WITHELIST}" >>
serverfiles/ts3-server.ini && \  
echo "query_ip_blacklist=${TS3_QUERY_IP_BLACKLIST}" >>
serverfiles/ts3-server.ini && \  
echo "dbplugin=${TS3_DB_PLUGIN}" >> serverfiles/ts3-server.ini && \  
echo "dbpluginparameter=${TS3_DB_PLUGIN_PARAMETER}" >>
serverfiles/ts3-server.ini && \  
echo "dbsqlpath=${TS3_DB_SQL_PATH}" >> serverfiles/ts3-server.ini && \  
echo "dbsqlcreatepath=${TS3_DB_SQL_CREATE_PATH}" >> serverfiles/ts3-server.ini
&& \  
echo "dbconnections=${TS3_DB_CONNECTIONS}" >> serverfiles/ts3-server.ini && \  
echo "logpath=${TS3_LOG_PATH}" >> serverfiles/ts3-server.ini && \  
echo "logquerycommands=${TS3_LOG_QUERY_COMMANDS}" >>
serverfiles/ts3-server.ini && \  
echo "dbclientkeepdays=${TS3_DB_CLIENT_KEEP_DAYS}" >>
serverfiles/ts3-server.ini && \  
echo "logappend=${TS3_LOG_APPEND}" >> serverfiles/ts3-server.ini && \  
echo "query_skipbruteforcecheck=${TS3_QUERY_SKIP_BRUTE_FORCE_CHECK}" >>
serverfiles/ts3-server.ini  
  
# Edit Server Script to hold Docker Environmental Varables  
RUN echo '[config]' > serverfiles/ts3db_mariadb.ini && \  
echo "host=${TS3_MYSQL_HOST}" >> serverfiles/ts3db_mariadb.ini && \  
echo "port=${TS3_MYSQL_PORT}" >> serverfiles/ts3db_mariadb.ini && \  
echo "username=${TS3_MYSQL_USER}" >> serverfiles/ts3db_mariadb.ini && \  
echo "password=${TS3_MYSQL_PASS}" >> serverfiles/ts3db_mariadb.ini && \  
echo "database=${TS3_MYSQL_DB}" >> serverfiles/ts3db_mariadb.ini && \  
echo "socket=${TS3_MYSQL_SOCKET}" >> serverfiles/ts3db_mariadb.ini  
  
# Make Start Script  
RUN echo '#!/bin/sh' > start.sh && \  
echo '' >> start.sh && \  
echo '# Docker Start / Run Script' > start.sh && \  
echo '' >> start.sh && \  
echo
'server_file="/home/ts3server/serverfiles/ts3server_minimal_runscript.sh"' >>
start.sh && \  
echo 'if [ -f "$server_file" ]' >> start.sh && \  
echo 'then' >> start.sh && \  
echo 'exec /home/ts3server/serverfiles/ts3server_minimal_runscript.sh
inifile=ts3-server.ini' >> start.sh && \  
echo 'else' >> start.sh && \  
echo './ts3server auto-install' >> start.sh && \  
echo 'exec /home/ts3server/serverfiles/ts3server_minimal_runscript.sh
inifile=ts3-server.ini' >> start.sh && \  
echo 'fi' >> start.sh && \  
chmod +x start.sh  
  
# Run Start Script  
CMD bash -c 'exec /home/ts3server/start.sh';  

