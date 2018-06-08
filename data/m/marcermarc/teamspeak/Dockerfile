######################  
# Downlaod Teamspeak #  
######################  
FROM alpine as download  
  
# --------------  
# Define version  
# --------------  
ARG VERSION=3.1.3  
  
# -------------------------------------  
# Download teamspeak  
# Unpack teamspeak  
# -------------------------------------  
RUN apk --update --no-cache add curl \  
&& mkdir /tmp/ts /opt \  
&& curl -o /tmp/ts/ts.tar.bz2
http://dl.4players.de/ts/releases/${VERSION}/teamspeak3-server_linux_amd64-${VERSION}.tar.bz2
\  
&& tar xjf /tmp/ts/ts.tar.bz2 -C /opt \  
&& mv /opt/teamspeak3-server_* /opt/teamspeak  
  
#######  
# Run #  
#######  
FROM frolvlad/alpine-glibc  
  
LABEL maintainer "docker@marcermarc.de"  
  
# ----------------------------------  
# Copy files from the download image  
# ----------------------------------  
COPY --from=download /opt/teamspeak /opt/teamspeak/  
  
# -------------------------------------  
# Add user teamspeak  
# -------------------------------------  
RUN apk --update --no-chache add ca-certificates \  
&& adduser -h /opt/teamspeak -S -D teamspeak \  
&& chown -R teamspeak /opt/teamspeak  
  
# ------------  
# Expose ports  
# ------------  
EXPOSE 9987/udp 30033/tcp 10011/tcp 2010/udp 41144/tcp 2008/tcp  
  
# -------------  
# Define volume  
# -------------  
VOLUME ["/mnt/teamspeak"]  
  
# ----------------  
# Set startup user  
# ----------------  
USER teamspeak  
  
# -------------------------------  
# Set the working directory  
# At this path the data is stored  
# -------------------------------  
WORKDIR /mnt/teamspeak  
  
# ----------------------------------------------------------  
# This enviroment-variable is set by the minimal-startscript  
# To start the server without the script it is set manual  
# ----------------------------------------------------------  
ENV LD_LIBRARY_PATH="/opt/teamspeak"  
  
# ------------------------------------------  
# Start the server with the created ini-file  
# ------------------------------------------  
ENTRYPOINT ["/opt/teamspeak/ts3server", "dbsqlpath=/opt/teamspeak/sql/",
"license_accepted=1"]

