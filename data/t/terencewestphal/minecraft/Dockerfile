FROM openjdk:alpine  
  
LABEL maintainer="Terence Westphal"  
  
# Use default value if the build argument is not set  
ARG VERSION=1.12.2  
ENV MC_VERSION=${VERSION}  
ENV PACKAGE="/opt/minecraft"  
ENV JAR="minecraft_server.${MC_VERSION}.jar"  
ENV JAR_OPT="nogui"  
ENV WORKDIR="/srv/minecraft"  
ENV PATH="${PACKAGE}/scripts:$PATH"  
# Update the system  
RUN apk upgrade --no-cache --purge -v  
  
# Download Minecraft Server  
ADD https://s3.amazonaws.com/Minecraft.Download/versions/${MC_VERSION}/${JAR}
${PACKAGE}/${JAR}  
  
# Add package content  
ADD ./defaults/* ${PACKAGE}/defaults/  
ADD ./scripts/* ${PACKAGE}/scripts/  
  
# Serve the content from the WORKDIR  
WORKDIR ${WORKDIR}  
  
# Expose the container's WORKDIR  
VOLUME ${WORKDIR}  
  
# Expose the container's network port  
EXPOSE 25565  
# Start the Minecraft server  
ENTRYPOINT ["start.sh"]

