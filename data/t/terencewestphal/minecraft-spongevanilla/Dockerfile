FROM terencewestphal/minecraft:1.12.2  
LABEL maintainer="Terence Westphal"  
  
# Use default value if the build argument is not set  
ARG VERSION=1.12.2-7.0.0-BETA-369  
ENV SPONGE_VERSION=${VERSION}  
ENV PACKAGE="/opt/minecraft"  
ENV JAR="spongevanilla-${SPONGE_VERSION}.jar"  
ENV JAR_OPT=""  
# Download Sponge Vanilla  
ADD
https://repo.spongepowered.org/maven/org/spongepowered/spongevanilla/${SPONGE_VERSION}/${JAR}
${PACKAGE}/${JAR}  
  
# Start the SpongeVanilla server  
ENTRYPOINT ["start.sh"]

