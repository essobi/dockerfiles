FROM ubuntu:latest  
MAINTAINER Gabriel Sentucq <perso@kazhord.fr>  
  
ENV version=1.0.5  
# Add dependencies  
RUN apt-get update && \  
apt-get install -y ca-certificates && \  
update-ca-certificates -f  
  
# Download grimd binary  
ADD
https://github.com/looterz/grimd/releases/download/v${version}/grimd_linux_x64
/bin/grimd  
  
# Chmod binary and add config folder  
RUN chmod a+x /bin/grimd && \  
mkdir -p ~/grimd/config && \  
ln -s ~/grimd/config /config  
  
# Copy custom config file to volume  
COPY grimd.toml ~/grimd/config/grimd.toml  
  
# Forward appropriate ports  
EXPOSE 53/udp 53/tcp 8080/tcp  
  
# Read grimd.toml from volume  
VOLUME ["/config"]  
  
# Run grimd  
ENTRYPOINT ["/bin/grimd", "-config", "~/grimd/config/grimd.toml", "-update"]  

