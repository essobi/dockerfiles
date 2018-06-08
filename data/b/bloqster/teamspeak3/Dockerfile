FROM debian:jessie  
MAINTAINER Michael Bortlik <Michael.Bortlik@gmail.com>  
  
# Set environment variables for build and entrypoint  
ENV TEAMSPEAK_VERSION="3.0.11.4" \  
TEAMSPEAK_DATAFOLDER="/etc/teamspeak3" \  
TEAMSPEAK_INSTALLDIR="/opt/teamspeak3"  
# Add user and group for the service to run under  
RUN groupadd -r teamspeak3 \  
&& useradd -r -g teamspeak3 teamspeak3  
  
# Install wget  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -r /var/lib/apt/lists/*  
  
# Download TS3 file and extract it into the install directory  
RUN mkdir -p ${TEAMSPEAK_INSTALLDIR} \  
&& curl -s
http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux-
amd64-${TEAMSPEAK_VERSION}.tar.gz \  
| tar -xvz -C ${TEAMSPEAK_INSTALLDIR} \--strip-components 1  
  
# Volume for persistent data and configuration files  
VOLUME ${TEAMSPEAK_DATAFOLDER}  
  
# Expose the TS3 Ports Default: 9987, ServerQuery: 10011, File: 30033  
EXPOSE 9987/udp 10011 30033  
# Add entrypoint script and set its permissions  
ADD /teamspeak3_entrypoint.sh /  
RUN chmod +x /teamspeak3_entrypoint.sh  
ENTRYPOINT ["/teamspeak3_entrypoint.sh"]

