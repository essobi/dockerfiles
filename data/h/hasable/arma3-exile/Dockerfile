# used to store resources that can neither been stored in github nor directly
download from external location.  
FROM hasable/arma3-resources:v2  
FROM hasable/a3-server:1.82  
LABEL maintainer='hasable'  
  
# Server user  
ARG USER_NAME=steamu  
ARG USER_UID=60000  
# Take long time, add it first to reuse cache  
USER root  
COPY cache /tmp/cache  
COPY \--from=0 / /tmp/cache  
RUN chown -R 60000:60000 /tmp/cache && ls /tmp/cache  
  
USER root  
RUN apt-get update \  
&& apt-get -y install curl libtbb2:i386 liblzo2-2 libvorbis0a libvorbisfile3
libvorbisenc2 libogg0 p7zip rename unzip \  
&& apt-get clean  
  
# Install stuff  
COPY sbin /usr/local/sbin  
WORKDIR /usr/local/sbin  
RUN chmod 500 * \  
&& sync \  
&& install-confd \  
&& install-depbo-tools  
  
# confd allows to modify config files according to different data sources,
including env vars.  
COPY conf/*.toml /etc/confd/conf.d/  
COPY conf/*.tpl /etc/confd/templates/  
  
# Provides commands & entrypoint  
COPY bin /usr/local/bin  
RUN chmod +x /usr/local/bin/*  
  
COPY keys /opt/arma3/keys  
RUN chown -R ${USER_UID}:${USER_UID} /opt/arma3/keys \  
&& chmod -R 755 /opt/arma3/keys  
  
# EXILE  
# Download and install Exile  
USER ${USER_NAME}  
WORKDIR /tmp  
RUN install-exile-server \  
&& install-exile \  
&& install-extended-base \  
&& install-admintoolkit \  
&& install-exad \  
&& install-advanced-towing \  
&& install-advanced-rappelling \  
&& install-advanced-urban-rappelling \  
&& install-cba \  
&& install-custom-loadout \  
&& install-custom-repair \  
&& install-enigma-revive \  
&& install-igiload  
  
# Temp fix for battleye  
WORKDIR /opt/arma3/battleye  
RUN cd /opt/arma3/battleye \  
&& for f in *.txt; do sed -i 's/^7\\(.*\\)/1\1/g' ${f}; done  
  
# MySQL default value  
ENV EXILE_DATABASE_HOST=mysql  
ENV EXILE_DATABASE_NAME=exile  
ENV EXILE_DATABASE_USER=exile  
ENV EXILE_DATABASE_PASS=password  
ENV EXILE_DATABASE_PORT=3306  
# Exile default value  
ENV EXILE_CONFIG_HOSTNAME="Exile Vanilla Server"  
ENV EXILE_CONFIG_PASSWORD=""  
ENV EXILE_CONFIG_PASSWORD_ADMIN="password"  
ENV EXILE_CONFIG_PASSWORD_COMMAND="password"  
ENV EXILE_CONFIG_PASSWORD_RCON="password"  
ENV EXILE_CONFIG_MAXPLAYERS=12  
ENV EXILE_CONFIG_VON=0  
ENV EXILE_CONFIG_MOTD="{\"Welcome to Arma 3 Exile Mod, packed by hasable with
Docker!\", \"This server is for test only, you should consider customizing
it.\", \"Enjoy your stay!\" }"  
ENV EXILE_CONFIG_MISSION="Exile.Altis"  
ENV EXILE_CONFIG_DIFFICULTY="ExileRegular"  
# interval de redemarrage, en seconde  
ENV EXILE_CONFIG_RESTART_CYCLE=14400  
# heure de demarrage du cycle, en seconde par rapport a minuit  
ENV EXILE_CONFIG_RESTART_START=0  
# ne pas redemarrer si le serveur a demarre depuis moins de Xs  
ENV EXILE_CONFIG_RESTART_GRACE_TIME=900  
USER ${USER_NAME}  
WORKDIR /opt/arma3  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint", "/opt/arma3/arma3server"]  
CMD ["\"-config=conf/exile.cfg\"", \  
"\"-servermod=@ExileServer;@AdminToolkitServer;@AdvancedRappelling;@AdvancedUrbanRappelling;@Enigma;@ExAd\"",
\  
"\"-mod=@Exile;@EBM;@CBA_A3\"", \  
"-bepath=/opt/arma3/battleye", \  
"-world=empty", \  
"-autoinit"]  

