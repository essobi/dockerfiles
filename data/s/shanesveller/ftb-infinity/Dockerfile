FROM shanesveller/minecraft:latest  
  
ENV PACK_ZIP
http://www.creeperrepo.net/FTB2/modpacks%5EFTBInfinity%5E2_5_0%5EFTBInfinityServer.zip  
RUN curl -o /tmp/minecraft.zip $PACK_ZIP && \  
unzip /tmp/minecraft.zip && \  
rm /tmp/minecraft.zip  
RUN sh FTBInstall.sh  
RUN echo "eula=true" > eula.txt  
  
ENV JVM_ARGS -server -Xms512M -Xmx2048M -XX:PermSize=256M -XX:+UseParNewGC
-XX:+CMSIncrementalPacing -XX:+CMSClassUnloadingEnabled
-XX:ParallelGCThreads=2 -XX:MinHeapFreeRatio=5 -XX:MaxHeapFreeRatio=10  
ENV JAR_NAME FTBServer-1.7.10-1614.jar  
  
VOLUME /opt/minecraft/world  
CMD java $JVM_ARGS -jar $JAR_NAME nogui  
  

