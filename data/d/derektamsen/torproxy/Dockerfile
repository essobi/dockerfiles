FROM debian:jessie  
  
# copy the gpg key in and install the services  
COPY config/release-key.txt /tmp/tor-release-key.txt  
RUN apt-key add /tmp/tor-release-key.txt && \  
echo "deb http://deb.torproject.org/torproject.org jessie main" | tee
/etc/apt/sources.list.d/tor.list  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
tor \  
deb.torproject.org-keyring \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY config/torrc /etc/tor/  
  
EXPOSE 9050  
RUN set -ex \  
&& /usr/bin/install -Z -m 02755 -o debian-tor -g debian-tor -d
/data/var/run/tor \  
&& /usr/bin/install -Z -m 02700 -o debian-tor -g debian-tor -d /data/tor \  
&& /usr/bin/tor \  
\--defaults-torrc /usr/share/tor/tor-service-defaults-torrc \  
-f /etc/tor/torrc \  
\--RunAsDaemon 0 \  
\--verify-config  
  
ENTRYPOINT ["/usr/bin/tor"]  
CMD ["-f", "/etc/tor/torrc", "--RunAsDaemon", "0"]  

