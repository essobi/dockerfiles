FROM openjdk:8-jre-alpine  
ARG VANILLA_VERSION=1.10.2  
ARG SPONGE_VERSION=5.2.0  
ARG SPONGE_RELEASE=BETA-393  
ARG LAUNCH_WRAPPER_VERSION=1.12  
  
LABEL maintainer="Yuxiang Zhu <vfreex@gmail.com>" \  
name=spongevanilla \  
version=${VANILLA_VERSION}-${SPONGE_VERSION} \  
release=${SPONGE_RELEASE}  
  
ARG SPONGEVANILLA_ROOT=/opt/spongevanilla  
ARG SPONGEVANILLA_WORKDIR=/var/local/spongevanilla  
ARG
SPONGEVANILLA_URL=https://repo.spongepowered.org/maven/org/spongepowered/spongevanilla/${VANILLA_VERSION}-${SPONGE_VERSION}-${SPONGE_RELEASE}/spongevanilla-${VANILLA_VERSION}-${SPONGE_VERSION}-${SPONGE_RELEASE}.jar  
ARG
VANILLA_URL=https://s3.amazonaws.com/Minecraft.Download/versions/${VANILLA_VERSION}/minecraft_server.${VANILLA_VERSION}.jar  
ARG
LAUNCHWRAPPER_URL=https://libraries.minecraft.net/net/minecraft/launchwrapper/${LAUNCH_WRAPPER_VERSION}/launchwrapper-${LAUNCH_WRAPPER_VERSION}.jar  
  
RUN apk --no-cache add \--virtual .build-deps ca-certificates wget \  
# install SpongeVanilla  
&& mkdir -p "$SPONGEVANILLA_ROOT" \  
&& wget "$SPONGEVANILLA_URL" -O "$SPONGEVANILLA_ROOT"/spongevanilla.jar \  
# install Vanilla server  
&& wget "$VANILLA_URL" -O
"$SPONGEVANILLA_ROOT/minecraft_server.${VANILLA_VERSION}.jar" \  
&& mkdir -p
"$SPONGEVANILLA_ROOT/libraries/net/minecraft/launchwrapper/${LAUNCH_WRAPPER_VERSION}"
\  
# install launchwrapper  
&& wget "$LAUNCHWRAPPER_URL" -O
"$SPONGEVANILLA_ROOT/libraries/net/minecraft/launchwrapper/${LAUNCH_WRAPPER_VERSION}/launchwrapper-${LAUNCH_WRAPPER_VERSION}.jar"
\  
# create workdir  
&& mkdir -p "$SPONGEVANILLA_WORKDIR" \  
&& chown -R nobody:root "$SPONGEVANILLA_WORKDIR" \  
&& chmod -R g+rwX "$SPONGEVANILLA_WORKDIR" \  
# clean up  
&& apk del .build-deps  
  
ENV SPONGEVANILLA_JAVA_OPTS='-Xms1G -Xmx2G' \  
SPONGEVANILLA_OPTS='--no-download'  
USER 9999  
WORKDIR "$SPONGEVANILLA_WORKDIR"  
COPY files/ /  
CMD ["/sponge-vanilla.sh"]  
  

