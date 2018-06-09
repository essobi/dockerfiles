# Thermos is a fork of KCauldron, a craftbukkit forge server for Minecraft.  
# README.md is Your friend (:  
FROM openjdk:8-jre-alpine  
  
MAINTAINER Arano-kai <captcha(dot)is.evil(meov)gmail.(You know what goes here
(:} )>  
  
# Additional pkgs  
RUN apk --no-cache add openssl tmux  
  
# Shortcuts and stuff, usually not for change (part 1)  
ENV THERMOS_USR="thermos"  
ENV THERMOS_HOME="/opt/${THERMOS_USR}"  
ENV THERMOS_WORKDIR="${THERMOS_HOME}/workdir" \  
THERMOS_TMUX_SNAME="MCConsole"  
# SECURITY: to avoid undiscovered vulnerabilities in java, thermos or any
mods/plugins,  
# we run server as unprivileged user  
RUN mkdir -p "${THERMOS_HOME}" \  
&& addgroup -S ${THERMOS_USR} \  
&& adduser -S -s /bin/sh -h "${THERMOS_HOME}" -g ${THERMOS_USR} -G
${THERMOS_USR} ${THERMOS_USR}  
  
# Script that implements properly startup and shutdown routines  
ADD entrypoint.sh /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
  
# Version setup  
ENV MINECRAFT_VER=1.7.10 \  
FORGE_VER=1614 \  
THERMOS_VER=58 \  
THERMOS_JAR_MD5=447dfdb45c4c39be88cc32590cc07649 \  
THERMOS_LIB_MD5=ffb77aec890ea9c8763821ff9fb590c2  
  
# Shortcuts and stuff, usually not for change (part 2)  
ENV THERMOS_JAR="Thermos-server.jar" \  
THERMOS_JAR_LNK="https://github.com/CyberdyneCC/Thermos/releases/download/${THERMOS_VER}/Thermos-${MINECRAFT_VER}-${FORGE_VER}-server.jar"
\  
THERMOS_LIB="libraries.zip"  
ENV
THERMOS_LIB_LNK="https://github.com/CyberdyneCC/Thermos/releases/download/${THERMOS_VER}/${THERMOS_LIB}"  
WORKDIR "${THERMOS_HOME}"  
  
# Download -> check -> unpack -> cleanup  
# `chown` & `find` statements prevent modifications and direct execution by
${THERMOS_USR}  
RUN wget -O ${THERMOS_JAR} ${THERMOS_JAR_LNK} \  
&& wget -O ${THERMOS_LIB} ${THERMOS_LIB_LNK} \  
&& THERMOS_JAR_MD5_OUT="$(md5sum ${THERMOS_JAR} | awk '{print($1)}')" \  
&& THERMOS_LIB_MD5_OUT="$(md5sum ${THERMOS_LIB} | awk '{print($1)}')" \  
&& if [ "${THERMOS_JAR_MD5}" = "${THERMOS_JAR_MD5_OUT}" ] && [
"${THERMOS_LIB_MD5}" = "${THERMOS_LIB_MD5_OUT}" ]; then \  
unzip -o ${THERMOS_LIB} \  
; rm -f ${THERMOS_LIB} \  
; chown -R root.root "${THERMOS_HOME}" \  
; find "${THERMOS_HOME}" -type d -exec chmod 755 "{}" \; \  
; find "${THERMOS_HOME}" -type f -exec chmod 644 "{}" \; \  
; else \  
>&2 printf '\n\t\t\t%s\t\t\t%s\n' "${THERMOS_JAR}" "${THERMOS_LIB}" \  
; >&2 printf '%s:\t%s\t%s\n' "Downloaded" "${THERMOS_JAR_MD5_OUT}"
"${THERMOS_LIB_MD5_OUT}" \  
"Expected" "${THERMOS_JAR_MD5}" "${THERMOS_LIB_MD5}" \  
; >&2 printf '\n%s\n' 'Please, re-run build or check corresponding vars.' \  
; exit 1 \  
; fi  
  
# Preparing workplace  
RUN mkdir -p "${THERMOS_WORKDIR}" \  
&& chown -R ${THERMOS_USR}.${THERMOS_USR} "${THERMOS_WORKDIR}"  
  
EXPOSE 25565  
VOLUME "${THERMOS_WORKDIR}"  
WORKDIR "${THERMOS_WORKDIR}"  
USER ${THERMOS_USR}  
  
# Set java opts that will be allways used  
# TODO: Create OOM dump with unique name  
ENV JVM_OPT_STRICT="-XX:+UseG1GC -XX:StringTableSize=1000003
-XX:MaxGCPauseMillis=50 -XX:+UseFastAccessorMethods -XX:+OptimizeStringConcat
-XX:+AggressiveOpts -XX:+UseStringDeduplication
-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=./logs/OOM_Dump_last.hprof
-XX:hashCode=5 -Dfile.encoding=UTF-8 -Dfml.debugExit=true"  
ENTRYPOINT ["entrypoint"]  
  
# This will be default java opts that can be overrided  
CMD ["-XX:MetaspaceSize=512M", "-XX:MaxMetaspaceSize=2G", "-Xms2G", "-Xmx4G"]  

