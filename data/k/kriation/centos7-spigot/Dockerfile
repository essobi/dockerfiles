FROM kriation/centos7-jre8 as spigot-builder  
ARG SPIGOT_VERSION=latest  
ENV SPIGOT_VERSION ${SPIGOT_VERSION:-latest}  
WORKDIR /tmp/spigot  
RUN yum install git && \  
curl -o BuildTools.jar
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
&& \  
java -jar BuildTools.jar -rev $SPIGOT_VERSION  
  
FROM kriation/centos7-jre8 as spigot-config  
ARG SPIGOT_VERSION=latest  
ARG MC_EULA=false  
ARG MC_SERVER_MEM=1024M  
ARG MC_SERVER_PORT=25565  
ARG MC_SERVER_QUERY=false  
ARG MC_SERVER_QUERY_PORT=25565  
ARG MC_SERVER_RCON=false  
ARG MC_SERVER_RCON_PORT=25567  
ARG MC_SERVER_RCON_PASS  
ENV SPIGOT_VERSION=${SPIGOT_VERSION:-latest} \  
MC_SERVER_MEM=${MC_SERVER_MEM:-1024M} \  
MC_SERVER_PORT=${MC_SERVER_PORT:-25565} \  
MC_SERVER_QUERY=${MC_SERVER_QUERY:-false} \  
MC_SERVER_QUERY_PORT=${MC_SERVER_QUERY_PORT:-25565} \  
MC_SERVER_RCON=${MC_SERVER_RCON:-false} \  
MC_SERVER_RCON_PORT=${MC_SERVER_RCON_PORT:-25567} \  
MC_SERVER_RCON_PASS=${MC_SERVER_RCON_PASS} \  
MC_EULA=${MC_EULA:-false}  
LABEL build-date="" \  
license="" \  
name="Spigot-$SPIGOT_VERSION" \  
vendor=""  
WORKDIR /opt/spigot  
COPY \--from=spigot-builder /tmp/spigot/spigot*.jar
/tmp/spigot-$SPIGOT_VERSION.jar  
COPY config/* /opt/spigot/  
RUN useradd -d /opt/spigot -M -U spigot && \  
mkdir -p /opt/spigot/{logs,plugins,worlds} && \  
chown -R spigot:spigot /opt/spigot  
USER spigot  
RUN sed -i 's/\\(server-port=\\)[[:print:]]*/\1'"$MC_SERVER_PORT"'/g'
server.properties && \  
sed -i 's/\\(enable-query=\\)[[:print:]]*/\1'"$MC_SERVER_QUERY"'/g'
server.properties && \  
sed -i 's/\\(enable-rcon=\\)[[:print:]]*/\1'"$MC_SERVER_RCON"'/g'
server.properties && \  
sed -i 's/\\(query.port=\\)[[:print:]]*/\1'"$MC_SERVER_QUERY_PORT"'/g'
server.properties && \  
sed -i 's/\\(rcon.port=\\)[[:print:]]*/\1'"$MC_SERVER_RCON_PORT"'/g'
server.properties && \  
sed -i 's/\\(rcon.password=\\)[[:print:]]*/\1'"$MC_SERVER_RCON_PASS"'/g'
server.properties  
EXPOSE $MC_SERVER_PORT $MC_SERVER_QUERY_PORT $MC_SERVER_RCON_PORT  
VOLUME /opt/spigot  
ENTRYPOINT java -Xms$MC_SERVER_MEM -XX:+UseG1GC
-Dcom.mojang.eula.agree=$MC_EULA -jar /tmp/spigot-$SPIGOT_VERSION.jar
--noconsole --world-dir /opt/spigot/worlds  

