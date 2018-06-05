FROM azul/zulu-openjdk-debian:latest  
MAINTAINER Adrian Haasler García <dev@adrianhaasler.com>  
  
# Configuration  
ENV STASH_HOME /data/stash  
ENV STASH_VERSION 3.11.2  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
tar \  
xmlstarlet  
  
# Create the user that will run the stash instance and his home directory
(also make sure that the parent directory exists)  
RUN mkdir -p $(dirname $STASH_HOME) \  
&& useradd -m -d $STASH_HOME -s /bin/bash -u 782 stash  
  
# Download and install stash in /opt with proper permissions and clean
unnecessary files  
RUN curl -Lks
http://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-$STASH_VERSION.tar.gz -o /tmp/stash.tar.gz \  
&& mkdir -p /opt/stash \  
&& tar -zxf /tmp/stash.tar.gz --strip=1 -C /opt/stash \  
&& chown -R root:root /opt/stash \  
&& chown -R 782:root /opt/stash/logs /opt/stash/temp /opt/stash/work \  
&& rm /tmp/stash.tar.gz  
  
# Add stash customizer and launcher  
COPY launch.sh /launch  
  
# Make stash customizer and launcher executable  
RUN chmod +x /launch  
  
# Expose ports  
EXPOSE 7990 7999  
# Workdir  
WORKDIR /opt/stash  
  
# Launch stash  
ENTRYPOINT ["/launch"]  

