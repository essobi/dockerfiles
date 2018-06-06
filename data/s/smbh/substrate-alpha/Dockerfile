FROM debian:stretch-slim  
  
ENV PATH=/opt/conda/bin:$PATH  
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions
-XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAMFraction=1 ${SUBSTRATE_JAVA_OPTS}"  
  
RUN mkdir -p /usr/share/man/man1/ \  
&& apt-get update --fix-missing \  
&& apt-get install -y build-essential ca-certificates bzip2 wget
openjdk-8-jre-headless nginx procps \  
&& apt-get install --no-install-recommends -y cron \  
&& echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh -O
~/miniconda.sh \  
&& /bin/bash ~/miniconda.sh -b -p /opt/conda \  
&& rm ~/miniconda.sh \  
&& PATH=/opt/conda/bin:$PATH pip install circus certbot awscli certbot-route53
\  
&& apt-get remove -y build-essential bzip2 wget \  
&& apt-get autoremove -y \  
&& rm /etc/nginx/sites-enabled/default \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -fr /tmp/*  

