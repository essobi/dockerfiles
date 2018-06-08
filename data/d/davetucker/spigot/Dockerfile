FROM java:8  
RUN apt-get update && apt-get install git-core  
WORKDIR /usr/src/spigot  
RUN wget -q
https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar  
RUN git config --global --unset core.autocrlf || true  
RUN java -jar BuildTools.jar  
VOLUME /etc/spigot  
WORKDIR /etc/spigot  
CMD ["java", "-jar", "-Xmx1024M", "-Xms1024M",
"/usr/src/spigot/spigot-1.8.8.jar"]  
EXPOSE 25565  

