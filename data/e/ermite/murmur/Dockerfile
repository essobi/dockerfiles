FROM alpine:3.5  
  
LABEL org.label-schema.maintainer = "Ermite Chevelu" \  
org.label-schema.name = "ermite/murmur" \  
org.label-schema.descritption = "Lightweight image with up-to-date Mumble
server." \  
org.label-schema.vcs-url = "https://github.com/Ermite-Chevelu/murmur/" \  
org.label-schema.version = "1.2.19" \  
org.label-schema.schema-version = "1.0" \  
org.label-schema.docker.cmd = "docker run -d -p 64738:64738/tcp -p
64738:64738/udp ermite/murmur"  
  
ARG MUMBLE_VERSION=1.2.19  
  
# Install mumble-server  
RUN apk add \--no-cache curl && \  
curl -L https://github.com/mumble-
voip/mumble/releases/download/${MUMBLE_VERSION}/murmur-
static_x86-${MUMBLE_VERSION}.tar.bz2 | tar -xj -C /tmp/ && \  
mkdir -p /usr/share/slice/ /var/lib/murmur/ && \  
mv /tmp/murmur-static_x86-${MUMBLE_VERSION}/murmur.x86 /usr/sbin/murmurd && \  
cp /tmp/murmur-static_x86-${MUMBLE_VERSION}/murmur.ini /etc/ && \  
cp /tmp/murmur-static_x86-${MUMBLE_VERSION}/ice/Murmur.ice /usr/share/slice/
&& \  
sed 's/^database=$/database=\/var\/lib\/murmur\/murmur.sqlite/' \  
-i /etc/murmur.ini || return 1 && \  
adduser -H -D -s /dev/null murmur && \  
chown murmur:murmur /var/lib/murmur/ && \  
apk del \--no-cache curl && \  
rm -rf /tmp/*  
  
# Mount volume for db data  
VOLUME /var/lib/murmur/  
# Expose apporpriate ports (mumble ports (tcp/udp), and Ice port)  
EXPOSE 64738/tcp \  
64738/udp \  
6502/tcp  
  
# Switch to non-root user to start murmur process  
USER murmur  
  
# Run murmur  
ENTRYPOINT ["/usr/sbin/murmurd", "-fg", "-v", "-ini", "/etc/murmur.ini"]  

