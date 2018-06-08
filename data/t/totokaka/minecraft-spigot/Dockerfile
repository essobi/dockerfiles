# minecraft-spigot  
#  
# An image for a Spigot Minecraft server  
# If this Dockerfile is used alone you will get a completely empty server  
# The intention is to have another Dockerfile having this as it's parent and  
# adding base server files through ADD statements.  
# We build off totokaka/minecraft-base  
FROM totokaka/minecraft-base  
  
MAINTAINER totokaka <mail@totokaka.io>  
  
# We need the spigot jar  
ADD http://ci.md-5.net/job/Spigot/lastSuccessfulBuild/artifact/Spigot-
Server/target/spigot.jar /minecraft/spigot.jar  
ADD args-split.sh /bin/args-split  
  
# For the entry point we use the args-split script.  
# The syntax for running the container is:  
# docker run -d -i -t totokaka/minecraft-spigot [<java args> \-- <spigot
args>]  
# The entry point is just starting the server.  
ENTRYPOINT ["/bin/args-split", "java", "--", "-jar", "spigot.jar", "--"]  
  
# Default command  
CMD ["-Xmx512M", "-Xms512M", "--", "nogui"]  

