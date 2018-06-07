FROM openjdk:8-jre-alpine  
MAINTAINER jurrian@argu.co  
  
ARG VERSION  
ARG EXIST_HOME  
  
ENV VERSION=${VERSION:-3.5.0} \  
MAX_MEMORY="1024" \  
EXIST_HOME=${EXIST_HOME:-/opt/exist}  
  
WORKDIR ${EXIST_HOME}  
ADD entrypoint.sh entrypoint.sh  
  
VOLUME ${EXIST_HOME}/webapp/WEB-INF/data/  
  
# eXistDB needs ant to automate common tasks like backup/restore or importing  
RUN apk --update add wget bash apache-ant \  
&& wget -q -O '/tmp/exist.jar'
"https://bintray.com/existdb/releases/download_file?file_path=eXist-db-
setup-$VERSION.jar" \  
&& echo "INSTALL_PATH=${EXIST_HOME}" > '/tmp/options.txt' \  
# ending with true because java somehow returns with a non-zero after
succesfull installing  
&& java -jar '/tmp/exist.jar' -options '/tmp/options.txt' || true \  
&& rm -f '/tmp/exist.jar' '/tmp/options.txt' \  
  
&& sed -i "s/Xmx%{MAX_MEMORY}m/Xmx\${MAX_MEMORY}m/g"
${EXIST_HOME}/bin/functions.d/eXist-settings.sh \  
# prefix java command with exec to force java being process 1 and receiving
docker signals  
&& sed -i 's/^\"${JAVA_RUN/exec \"${JAVA_RUN/' ${EXIST_HOME}/bin/startup.sh \  
  
# alpine has no locale binary, this will fix that  
&& printf "#!/bin/sh\necho $LANG" > /usr/bin/locale \  
&& chmod +x entrypoint.sh /usr/bin/locale  
  
# override the main configuration  
ADD conf.xml conf.xml  
  
CMD ${EXIST_HOME}/entrypoint.sh  
  
EXPOSE 8080 8443  

