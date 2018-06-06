FROM debian:jessie  
MAINTAINER Daniel Kühne <dkhmailto@googlemail.com>  
  
ENV TMATE_HOME=/tmate-slave  
  
RUN set -x && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends curl
ca-certificates openssh-client libevent-2.0 libutempter0 libncurses5 zlib1g
libssl1.0.0 && \  
mkdir -p $TMATE_HOME/keys && \  
curl -sSL "https://raw.githubusercontent.com/tmate-io/tmate-
slave/master/create_keys.sh" -o $TMATE_HOME/create_keys.sh && \  
chmod 755 $TMATE_HOME/create_keys.sh && \  
curl -sSL "https://circle-artifacts.com/gh/dakue/docker-tmate-slave-
builder/1/artifacts/0/tmp/circle-artifacts.kTAa6Wz/tmate-slave" -o
/usr/local/bin/tmate-slave && \  
chmod 755 /usr/local/bin/tmate-slave && \  
curl -sSL "https://circle-artifacts.com/gh/dakue/docker-tmate-slave-
builder/1/artifacts/0/tmp/circle-artifacts.kTAa6Wz/tmate-slave-lib.tar.gz" | \  
tar xz && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY message.sh $TMATE_HOME/  
RUN chmod +x $TMATE_HOME/message.sh  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 2222  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["tmate-slave"]  
  

