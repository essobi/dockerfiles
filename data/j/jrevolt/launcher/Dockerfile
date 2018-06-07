FROM jrevolt/jre  
  
RUN apk --no-cache --update add bash  
  
ARG VERSION="0.2.1"  
ARG
URLJAR="http://repo.jrevolt.io/content/groups/public/io/jrevolt/launcher/io.jrevolt.launcher/${VERSION}/io.jrevolt.launcher-${VERSION}.jar"  
ARG
URLEXE="https://raw.githubusercontent.com/jrevolt/io.jrevolt.launcher/dist/jrevolt.sh"  
  
ARG APPNAME="jrevolt"  
ARG HOMEDIR="/opt/${APPNAME}"  
ARG BINDIR="/usr/local/bin"  
ARG SCRIPT="${BINDIR}/jrevolt.sh"  
ARG JAR="${BINDIR}/io.jrevolt.launcher-${VERSION}.jar"  
RUN \  
mkdir -p ${HOMEDIR} && mkdir -p ${BINDIR} && mkdir -p ${HOMEDIR}/.jrevolt && \  
addgroup jrevolt && \  
adduser -S -D -h ${HOMEDIR} -s /bin/bash jrevolt jrevolt  
  
RUN \  
apk --no-cache --update add bash curl && \  
curl -sk -o ${SCRIPT} ${URLEXE} && chmod a+x ${SCRIPT} && \  
curl -sk -o ${JAR} ${URLJAR} && \  
chown -R jrevolt:jrevolt ${HOMEDIR} && \  
apk --purge del curl  
  
ENV HOME="${HOMEDIR}"  
ENV JREVOLT_LAUNCHER_JAR="${JAR}"  
  
VOLUME ["${HOME}/.jrevolt"]  
ENTRYPOINT ["jrevolt.sh"]  
  
  

