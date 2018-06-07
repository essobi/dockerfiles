FROM openjdk:8-jre-alpine  
  
ARG SPONGE_VERSION=1.10.2-2281-5.2.0-BETA-2401  
ARG FORGE_VERSION=1.10.2-12.18.3.2281  
  
LABEL \  
name=spongeforge \  
version="$SPONGE_VERSION" \  
maintainer='Yuxiang Zhu <vfreex@gmail.com>'  
  
ENV SPONGE_WORKSPACE=/var/local/sponge \  
SPONGE_ROOT=/opt/sponge \  
SPONGE_USER=sponge \  
SPONGE_GROUP=sponge \  
SPONGE_VERSION="$SPONGE_VERSION" \  
FORGE_VERSION="$FORGE_VERSION" \  
JAVA_OPTS='-Xms1G -Xmx2G'  
  
RUN \  
apk update \  
&& apk add --virtual build-deps wget ca-certificates \  
# install SpongeForge  
&& mkdir -p "$SPONGE_ROOT"/mods \  
&& wget -O "$SPONGE_ROOT/mods/spongeforge-$SPONGE_VERSION.jar"
"https://repo.spongepowered.org/maven/org/spongepowered/spongeforge/$SPONGE_VERSION/spongeforge-$SPONGE_VERSION.jar"
\  
# install Vanilla  
&& MINECRAFT_VERSION=$(echo "$SPONGE_VERSION" | cut -d - -f 1) \  
&& wget -O "$SPONGE_ROOT/minecraft_server.$MINECRAFT_VERSION.jar"
https://s3.amazonaws.com/Minecraft.Download/versions/"$MINECRAFT_VERSION"/minecraft_server."$MINECRAFT_VERSION".jar
\  
# install forge  
&& cd "$SPONGE_ROOT/" \  
&& wget -O "$SPONGE_ROOT/forge-$FORGE_VERSION-installer.jar"
"http://files.minecraftforge.net/maven/net/minecraftforge/forge/$FORGE_VERSION/forge-$FORGE_VERSION-
installer.jar" \  
&& java -jar "$SPONGE_ROOT/forge-$FORGE_VERSION-installer.jar"
\--installServer "$SPONGE_ROOT/" \  
&& ln -s "$SPONGE_ROOT/forge-$FORGE_VERSION-universal.jar"
"$SPONGE_ROOT/forge-universal.jar" \  
&& rm "$SPONGE_ROOT/forge-$FORGE_VERSION-installer.jar" "$SPONGE_ROOT/"*.log \  
# create user and workspace  
&& addgroup -S "$SPONGE_GROUP" \  
&& adduser -G "$SPONGE_GROUP" -S "$SPONGE_USER" \  
&& mkdir -p "$SPONGE_WORKSPACE" \  
&& chown -R "$SPONGE_USER":"$SPONGE_GROUP" "$SPONGE_WORKSPACE" \  
# install utils  
&& apk add su-exec tini \  
# clean up  
&& apk del build-deps \  
&& rm -rf /var/lib/apk/  
  
COPY files/ /  
  
WORKDIR "$SPONGE_WORKSPACE"  
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/sbin/entrypoint.sh"]  
CMD ["/usr/local/bin/spongeforge"]  
VOLUME "$SPONGE_WORKSPACE"  

