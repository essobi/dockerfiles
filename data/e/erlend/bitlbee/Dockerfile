FROM debian:jessie  
  
COPY sources.list /etc/apt/sources.list.d/bitlbee.list  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apt-get update -q && \  
apt-get install -y curl && \  
(curl -L https://jgeboski.github.io/obs.key | apt-key add -) && \  
(curl -L https://code.bitlbee.org/debian/release.key | apt-key add -) && \  
apt-get update -q && \  
apt-get install -y bitlbee-facebook && \  
apt-get autoremove --purge -y curl && \  
rm -rf /var/lib/apt/lists/*  
  
# Configure bitlbee  
RUN sed -e 's/[# ]*\\(RunMode =\\).*/\1 ForkDaemon/' \  
-e 's/[# ]*\\(DaemonInterface .*\\)/\1/' \  
-i /etc/bitlbee/bitlbee.conf  
  
VOLUME /var/lib/bitlbee  
EXPOSE 6667  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bitlbee", "-n"]  

