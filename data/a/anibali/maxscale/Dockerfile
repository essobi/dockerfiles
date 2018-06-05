FROM debian:jessie  
  
# Run Tini as PID 1, allowing us to send signals like SIGTERM to the command  
# we decide to run.  
ENV TINI_VERSION v0.8.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Download MaxScale Debian package and verify integrity  
ADD https://github.com/anibali/maxscale-
deb/releases/download/v1.2.1/maxscale_1.2.1_amd64.deb .  
COPY maxscale.md5 .  
RUN md5sum -c maxscale.md5 && rm maxscale.md5  
  
# Install MaxScale  
RUN apt-get update \  
&& apt-get install -y libaio1 libcurl3 libssl1.0.0 \  
&& rm -rf /var/lib/apt/lists/* \  
&& dpkg -i maxscale_1.2.1_amd64.deb \  
&& rm maxscale_1.2.1_amd64.deb  
  
# Copy config template into the image  
COPY maxscale.cnf.template /etc/  
  
# Copy start script into the image  
COPY start_maxscale.sh /  
  
# Expose Splitter Listener port  
EXPOSE 3306  
CMD ["/start_maxscale.sh"]  

