FROM maven:3-jdk-8-alpine  
MAINTAINER info@cubeengine.org  
  
# Th env variables of the next three layers are used for the image creation
process.  
# Setting them for a container shouldn't have any effect. With the exception
of a non working container ;)  
ENV MINECRAFT_VERSION=1.12.2 \  
# "bleeding" or "stable"  
SPONGE_TYPE="stable" \  
USER_NAME="minecraft"  
  
ENV MINECRAFT_DIR="/home/${USER_NAME}/server" \  
SCRIPT_DIR="/scripts"  
  
ENV SERVER_JAR="${MINECRAFT_DIR}/server.jar" \  
MINECRAFT_MODS_DIR="${MINECRAFT_DIR}/mods" \  
MINECRAFT_STATIC_MODS_DIR="${MINECRAFT_DIR}/static_mods" \  
MINECRAFT_CE_PLUGINS_DIR="${MINECRAFT_DIR}/ce-plugins" \  
MINECRAFT_CONFIG_DIR="${MINECRAFT_DIR}/config" \  
MINECRAFT_WORLD_DIR="${MINECRAFT_DIR}/world" \  
MINECRAFT_LOGS_DIR="${MINECRAFT_DIR}/logs" \  
MINECRAFT_ROOT_STUFF_DIR="${MINECRAFT_DIR}/root"  
  
ENV SPONGE_FILE="${MINECRAFT_STATIC_MODS_DIR}/sponge.jar"  
# Upgrading system and install some software  
RUN apk update && \  
apk upgrade && \  
apk --update add curl ca-certificates grep coreutils jq bash git  
  
# Create user and group  
RUN adduser -D -u 4928 "${USER_NAME}"  
USER "${USER_NAME}:${USER_NAME}"  
# Install server  
COPY maven/settings.xml /usr/share/maven/conf/settings.xml  
COPY scripts/builder/install_forge_sponge.sh
${SCRIPT_DIR}/install_forge_sponge.sh  
RUN bash ${SCRIPT_DIR}/install_forge_sponge.sh  
COPY scripts/builder/install_ce.sh ${SCRIPT_DIR}/install_ce.sh  
RUN bash ${SCRIPT_DIR}/install_ce.sh  
  
COPY scripts/runtime ${SCRIPT_DIR}  
RUN mkdir -p "${MINECRAFT_MODS_DIR}" && \  
mkdir -p "${MINECRAFT_CONFIG_DIR}" && \  
mkdir -p "${MINECRAFT_WORLD_DIR}" && \  
mkdir -p "${MINECRAFT_LOGS_DIR}" && \  
mkdir -p "${MINECRAFT_ROOT_STUFF_DIR}" && \  
chmod -R o+rwx "${MINECRAFT_DIR}"  
  
EXPOSE 25565/tcp 25575/tcp  
VOLUME ["${MINECRAFT_MODS_DIR}", "${MINECRAFT_CONFIG_DIR}",
"${MINECRAFT_WORLD_DIR}", "${MINECRAFT_LOGS_DIR}",
"${MINECRAFT_ROOT_STUFF_DIR}"]  
WORKDIR ${MINECRAFT_DIR}  
ENTRYPOINT bash ${SCRIPT_DIR}/entrypoint.sh  
  
# This environment variables can be used to control the server.  
ENV JAVA_VM_ARGS="" \  
# lists the plugins which shall be activated. an empty or unset string results
in a server containing all plugins  
# example "roles worlds vanillaplus fun fly"  
CE_PLUGINS="" \  
# Database settings. Supported Databases are MySQL, Sqlite and H2  
DB_HOST=localhost \  
DB_PORT=3306 \  
DB_USER=minecraft \  
DB_PASSWORD="" \  
DB_NAME=minecraft \  
DB_TABLE_PREFIX=cube_ \  
DB_LOG_DATABASE_QUERIES=false \  
# Mongo DB settings. Used by the bigdata plugin.  
MONGO_DB_HOST=localhost \  
MONGO_DB_PORT=27017 \  
MONGO_DB_USER=minecraft \  
MONGO_DB_PASSWORD="" \  
MONGO_DB_NAME=cubeengine \  
MONGO_DB_CONNECTION_TIMEOUT=5000 \  
# The next env variables control the server.properties file. Have a look at
the documentation of the file to get the meaning.  
ALLOW_FLIGHT=false \  
ALLOW_NETHER=true \  
ANNOUNCE_PLAYER_ACHIEVEMENTS=true \  
DIFFICULTY=1 \  
ENABLE_QUERY=false \  
ENABLE_RCON=false \  
ENABLE_COMMAND_BLOCK=false \  
FORCE_GAMEMODE=false \  
GAMEMODE=0 \  
GENERATE_STRUCTURES=true \  
GENERATOR_SETTINGS="" \  
HARDCORE=false \  
LEVEL_NAME=world \  
LEVEL_SEED="" \  
LEVEL_TYPE=DEFAULT \  
MAX_BUILD_HEIGHT=256 \  
MAX_PLAYERS=20 \  
MAX_TICK_TIME=60000 \  
MAX_WORLD_SIZE=29999984 \  
MOTD="A Minecraft Server" \  
NETWORK_COMPRESSION_THRESHOLD=256 \  
ONLINE_MODE=true \  
OP_PERMISSION_LEVEL=4 \  
PLAYER_IDLE_TIMEOUT=0 \  
PVP=true \  
RCON_PASSWORD="" \  
RESOURCE_PACK="" \  
RESOURCE_PACK_HASH="" \  
SNOOPER_ENABLED=true \  
SPAWN_ANIMALS=true \  
SPAWN_MONSTERS=true \  
SPAWN_NPCS=true \  
SPAWN_PROTECTION=16 \  
VIEW_DISTANCE=10 \  
WHITE_LIST=false \  

