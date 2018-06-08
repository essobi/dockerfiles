FROM debian:testing  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
# Set up matrix-synapse user. This goes first so the UID remains constant.  
RUN adduser --system --shell /usr/sbin/nologin --gecos 'Matrix Synapse User' \  
\--home /var/lib/matrix-synapse --no-create-home --group \  
\--disabled-password matrix-synapse  
  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef \  
-o Dpkg::Options::=--force-confold --purge install curl gnupg2 \  
apt-transport-https  
ADD matrix-repo-key.asc /etc/apt/matrix-repo-key.asc  
ADD matrix-repo.list /etc/apt/sources.list.d/matrix-repo.list  
RUN apt-key add /etc/apt/matrix-repo-key.asc && apt-get -q -y update && \  
apt-get -q -y -o Dpkg::Options::=--force-confdef \  
-o Dpkg::Options::=--force-confold --purge install matrix-synapse \  
python-psycopg2 python3-psycopg2 python-lxml python3-lxml \  
matrix-synapse-angular-client  
  
VOLUME ["/etc/matrix-synapse/base", "/etc/matrix-synapse/conf.d", \  
"/etc/matrix-synapse/secrets.d", "/var/lib/matrix-synapse", \  
"/etc/matrix-synapse/secrets", "/tls"]  
  
USER matrix-synapse  
ENTRYPOINT ["/usr/bin/python", "-m", "synapse.app.homeserver"]  
CMD ["--config-path=/etc/matrix-synapse/base/homeserver.yaml", \  
"--config-path=/etc/matrix-synapse/conf.d/", \  
"--config-path=/etc/matrix-synapse/secrets.d/"]  

