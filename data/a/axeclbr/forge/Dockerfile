FROM axeclbr/java:jre8  
  
WORKDIR /opt/forge  
  
RUN apk --update add curl \  
&& curl -L
"http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.6.4-9.11.1.1345/forge-1.6.4-9.11.1.1345-installer.jar"
-o /opt/forge/forge-installer.jar \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/lib/libc.musl-x86_64.so.1 \  
&& ln -s /lib/libz.so.1 /usr/lib/libz.so.1 \  
&& ln -s /opt/forge/minecraftforge-universal-1.6.4-9.11.1.1345.jar
/opt/forge/minecraft.jar \  
&& java -jar /opt/forge/forge-installer.jar \--installServer \  
&& apk del curl \  
&& rm -rf \  
/opt/forge/forge-installer.jar \  
/var/cache/apk/*  
  
WORKDIR /data  
VOLUME /data  
  
EXPOSE 25565  
  
CMD ["java", "-jar", "/opt/forge/minecraft.jar"]  

