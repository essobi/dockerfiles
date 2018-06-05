FROM postgres:10  
  
ADD archivecp /opt/memory-alpha/archivecp  
ADD basebackup /opt/memory-alpha/basebackup  
ADD init-backup.sh /docker-entrypoint-initdb.d/init-backup.sh  
ADD circus.ini /srv/circus.ini  
  
RUN chown -R postgres /opt/memory-alpha \  
&& chgrp -R postgres /opt/memory-alpha \  
&& mv /usr/local/bin/docker-entrypoint.sh /usr/local/bin/docker-entrypoint-
postgresql.sh \  
&& mkdir -p /usr/share/man/man1/ \  
&& apt-get update \--fix-missing \  
&& apt-get install -y bzip2 sudo wget build-essential \  
&& apt-get install --no-install-recommends -y cron anacron \  
&& echo 'export PATH=/opt/conda/bin:$PATH' >> /root/.bashrc \  
&& wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh \  
&& PATH=/opt/conda/bin:$PATH pip install circus awscli \  
&& apt-get remove -y build-essential wget \  
&& apt-get autoremove -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ADD certbot-cron /etc/cron.d/certbot-cron  

