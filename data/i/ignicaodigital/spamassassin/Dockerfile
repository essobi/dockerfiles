FROM debian:jessie-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -yq spamassassin razor  
  
RUN groupadd spamassassin && \  
useradd -g spamassassin -s /bin/false -d /var/log/spamassassin spamassassin &&
\  
mkdir -p /var/log/spamassassin && \  
mkdir -p /var/spamassassin && \  
mkdir -p /etc/spamassassin/.razor && \  
chown -R spamassassin:spamassassin /etc/spamassassin/.razor && \  
chown -R spamassassin:spamassassin /var/spamassassin && \  
chown -R spamassassin:spamassassin /var/log/spamassassin  
  
ADD local.cf /etc/spamassassin/local.cf  
  
RUN razor-admin -home=/etc/spamassassin/.razor -register  
RUN razor-admin -home=/etc/spamassassin/.razor -create  
RUN razor-admin -home=/etc/spamassassin/.razor -discover  
  
CMD ["spamd", "--username", "spamassassin", "--nouser-config", "-i",
"0.0.0.0", "--allowed-ips", "0.0.0.0/0"]  

