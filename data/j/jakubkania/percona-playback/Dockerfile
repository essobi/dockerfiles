FROM ubuntu:13.04  
#http://askubuntu.com/a/91821  
RUN sed -i -re 's/([a-z]{2}\\.)?archive.ubuntu.com|security.ubuntu.com/old-
releases.ubuntu.com/g' /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -qq wget ca-certificates\  
&& wget https://www.percona.com/downloads/Percona-Playback/Percona-
Playback-0.7/deb/raring/x86_64/percona-playback_0.7-211.raring_amd64.deb \  
&& dpkg -i percona-playback_0.7-211.raring_amd64.deb \  
&& rm percona-playback_0.7-211.raring_amd64.deb \  
|| apt-get install -fqq \  
&& rm -rf /var/lib/apt/lists/*  

