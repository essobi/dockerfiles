FROM rtrap/debian:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
gpg \  
libio-socket-ip-perl \  
libmail-dkim-perl \  
libnet-ident-perl \  
libsocket-getaddrinfo-perl \  
pyzor \  
razor \  
spamassassin \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/spamassassin/sa-update-keys \  
&& chmod 700 /etc/spamassassin/sa-update-keys \  
&& chown debian-spamd:debian-spamd /etc/spamassassin/sa-update-keys \  
&& mkdir -p /var/lib/spamassassin/.pyzor \  
&& chmod 700 /var/lib/spamassassin/.pyzor \  
&& echo "public.pyzor.org:24441" > /var/lib/spamassassin/.pyzor/servers \  
&& chmod 600 /var/lib/spamassassin/.pyzor/servers \  
&& chown -R debian-spamd:debian-spamd /var/lib/spamassassin/.pyzor  
  
RUN sed -i 's/^logfile = .*$/logfile = \/dev\/stderr/g' /etc/razor/razor-
agent.conf  
  
COPY conf/spamd.sh /  
COPY conf/rule-update.sh /  
COPY conf/run.sh /  
  
EXPOSE 783  
  
CMD ["/run.sh"]  

