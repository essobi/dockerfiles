# Pandoc and Kindlegen for publishing  
FROM debian:stable-slim  
  
LABEL maintainer "https://github.com/JenniferMack/docker-pandoc"  
  
# Update this to trigger new build  
ENV PANDOC_VER "1.19.2.1"  
ENV APT_CMD "apt-get install --yes --no-install-recommends"  
# App installs  
RUN apt-get update \  
&& $APT_CMD curl ca-certificates git make zip ruby ruby-sass \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Gems  
RUN gem install pandoc-ruby  
  
# Install Kindlegen  
RUN curl -sf
http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz \  
| tar xzf - kindlegen && mv kindlegen /usr/local/bin  
  
# Install Pandoc latest  
RUN curl -Lsf
https://github.com/jgm/pandoc/releases/download/$PANDOC_VER/pandoc-$PANDOC_VER-1-amd64.deb
\  
-o /tmp/pandoc.deb  
RUN dpkg -i /tmp/pandoc.deb && rm /tmp/pandoc.deb /usr/bin/pandoc-citeproc  
  
CMD ["bash"]  

