FROM bluetooth/minecraft-server  
  
MAINTAINER BlueTooth  
  
CMD wget --output-document=forge-installer.jar
http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.10.2-12.18.3.2422/forge-1.10.2-12.18.3.2422-installer.jar
&& \  
java -jar forge-installer.jar --installServer && \  
java -Xmx4096M -Xms4096M -jar forge-1.10.2-12.18.3.2422-universal.jar nogui  

