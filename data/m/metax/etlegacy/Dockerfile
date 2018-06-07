############################################################  
# Dockerfile to run ET: Legacy containers  
# Based on Debian image  
############################################################  
FROM debian:stretch  
MAINTAINER Christian Simon <mail@christiansimon.eu>  
  
ENV APP_USER etded  
ENV APP_USER_ID 800  
ENV APP_HOME /opt/etlegacy  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
# Install prerequisites and add dedicated user  
RUN apt-get update && apt-get install -y \  
p7zip-full \  
curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd -r --gid "${APP_USER_ID}" "${APP_USER}" \  
&& useradd -r --uid "${APP_USER_ID}" -g "${APP_USER}" -m "${APP_USER}" \  
&& mkdir -p "${APP_HOME}" \  
&& chown "${APP_USER}":"${APP_USER}" "${APP_HOME}" \  
&& chmod a+x /usr/local/bin/entrypoint.sh  
  
# Set the user to run etlegacy as daemon  
USER ${APP_USER}  
WORKDIR ${APP_HOME}  
  
# Install Wolfenstein: Enemy Territory Legacy  
RUN ( curl https://www.etlegacy.com/download/file/87 | tar xvz --strip-
components=1 ) \  
&& ( curl -o temp.exe
http://trackbase.eu/files//et/full/WolfET_2_60b_custom.exe; 7z e temp.exe
-o${APP_HOME}/etmain etmain/pak*.pk3; rm temp.exe ) \  
&& echo "set sv_allowDownload \"1\"" >> ${APP_HOME}/etmain/etl_server.cfg \  
&& echo "set rconpassword \"etlegacy\"" >> ${APP_HOME}/etmain/etl_server.cfg \  
&& mv ${APP_HOME}/etmain/etl_server.cfg
${APP_HOME}/etmain/etl_server_default.cfg \  
&& mkdir ${APP_HOME}/conf  
  
# Port to expose  
EXPOSE 27960/udp  
  
# Volume for server config  
VOLUME ${APP_HOME}/conf  
  
# Set the entrypoint to entrypoint  
ENTRYPOINT /usr/local/bin/entrypoint.sh  

