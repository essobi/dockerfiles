FROM openjdk:8-alpine AS staging  
  
ARG
DOWNLOADER=https://jenkins.dries007.net/job/CurseModpackDownloader/20/artifact/build/libs/CurseModpackDownloader-1.0.8.20-all.jar  
ARG MODPACK=https://minecraft.curseforge.com/projects/age-of-
engineering/files/2481115/download  
  
ADD $DOWNLOADER CurseModpackDownloader.jar  
  
ENV MODPACK=$MODPACK  
RUN java -jar CurseModpackDownloader.jar -i "$MODPACK" -o minecraft server
--eula | tee CurseModpackDownloader.out && \  
rm -f minecraft/CurseModpackDownloader.txt minecraft/*.log  
  
COPY start minecraft/  
  
RUN jar="$(grep '^The server installed successfully, you should now be able to
run the file ' CurseModpackDownloader.out | sed 's/^The server installed
successfully, you should now be able to run the file //')" && \  
cd minecraft/ && \  
awk -v jar="$jar" '{if (/^jar=/) print "jar=\"" jar "\""; else print}' start >
start.tmp && cat start.tmp > start && rm start.tmp && \  
mkdir state_hist && for i in logs backups crash-reports; do mkdir
"state_hist/$i" && ln -s "state_hist/$i"; done && \  
mkdir state && \  
mkdir state/world && ln -s state/world && \  
for i in server.properties whitelist.json ops.json banned-ips.json banned-
players.json; do ln -s "state/$i"; done  
  
FROM openjdk:8-alpine  
  
COPY \--from=staging minecraft /home/minecraft  
  
WORKDIR /home/minecraft  
  
RUN addgroup minecraft && adduser -SG minecraft minecraft && chown -R
minecraft:minecraft .  
  
USER minecraft  
  
VOLUME ["/home/minecraft/state", "/home/minecraft/state_hist"]  
EXPOSE 25565  
CMD /home/minecraft/start  
  
LABEL curse.modpack=age-of-engineering \  
curse.modpack.version=1.1.1c \  
minecraft.version=1.10.2 \  
forge.version=12.18.3.2477  

