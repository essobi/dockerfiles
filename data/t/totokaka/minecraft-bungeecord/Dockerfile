# minecraft-bungeecord  
#  
# An image for a BungeeCord Minecraft server proxy  
# If this Dockerfile is used alone you will get a completely empty proxy  
# The intention is to have another Dockerfile having this as it's parent and  
# adding base server files through ADD statements.  
# We build off totokaka/minecraft-base  
FROM totokaka/minecraft-base  
  
MAINTAINER totokaka <mail@totokaka.io>  
  
# We need the bungeecord jar  
ADD
http://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar
/minecraft/bungeecord.jar  
  
# For the entry point we use the args-split script.  
# The syntax for running the container is:  
# docker run -d -i -t totokaka/minecraft-bungeecord [<java args> \--
<bungeecord args>]  
# The entry point is just starting the server.  
ENTRYPOINT ["/bin/args-split", "java", "--", "-jar", "bungeecord.jar", "--"]  
  
# Default command  
CMD ["-Xmx256M", "-Xms256M", "--", ""]  

