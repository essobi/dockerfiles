FROM openjdk:10-jdk AS build  
  
RUN mkdir -p /usr/src/mods/jars  
RUN mkdir -p /usr/src/mods/compiled  
  
COPY . /usr/src  
WORKDIR /usr/src  
  
RUN javac -Xlint:unchecked -d /usr/src/mods/compiled --module-source-path
/usr/src/src $(find src -name "*.java")  
RUN jar --create --file /usr/src/mods/jars/joostvdg.dui.logging.jar --module-
version 1.0 -C /usr/src/mods/compiled/joostvdg.dui.logging .  
RUN jar --create --file /usr/src/mods/jars/joostvdg.dui.api.jar --module-
version 1.0 -C /usr/src/mods/compiled/joostvdg.dui.api .  
RUN jar --create --file /usr/src/mods/jars/joostvdg.dui.client.jar --module-
version 1.0 -C /usr/src/mods/compiled/joostvdg.dui.client .  
RUN jar --create --file /usr/src/mods/jars/joostvdg.dui.server.jar --module-
version 1.0 -e com.github.joostvdg.dui.server.cli.DockerApp\  
-C /usr/src/mods/compiled/joostvdg.dui.server .  
  
RUN rm -rf /usr/bin/dui-image  
RUN jlink --module-path /usr/src/mods/jars/:/${JAVA_HOME}/jmods \  
\--add-modules joostvdg.dui.api \  
\--add-modules joostvdg.dui.logging \  
\--add-modules joostvdg.dui.server \  
\--add-modules joostvdg.dui.client \  
\--launcher dui=joostvdg.dui.server \  
\--output /usr/bin/dui-image  
  
RUN ls -lath /usr/bin/dui-image  
RUN ls -lath /usr/bin/dui-image  
RUN /usr/bin/dui-image/bin/java --list-modules  
  
FROM debian:stable-slim  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="0.3.0"  
LABEL description="Docker image for playing with java applications in a
concurrent, parallel and distributed manor."  
# Add Tini - it is already included:
https://docs.docker.com/engine/reference/commandline/run/  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "-vv","-g", "--",
"/usr/bin/dui/bin/dui","-XX:+UseCGroupMemoryLimitForHeap",
"-XX:+UnlockExperimentalVMOptions"]  
ENV DATE_CHANGED="20180120-1525"  
HEALTHCHECK \--interval=12s --start-period=12s --timeout=20s CMD wget
--server-response http://localhost:8888 -O ip-current 2>&1| grep -c 'HTTP/1.1
200 OK'  
RUN apt-get update && apt-get install --no-install-recommends -y psmisc=22.*
wget=1.* && rm -rf /var/lib/apt/lists/*  
COPY \--from=build /usr/bin/dui-image/ /usr/bin/dui  
RUN /usr/bin/dui/bin/java --list-modules  
  

