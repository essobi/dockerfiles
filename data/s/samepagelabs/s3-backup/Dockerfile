FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y python3 wget python-pip pbzip2 \  
&& pip install awscli \  
&& apt-get clean \  
&& rm -vrf /var/lib/apt/lists/ /var/cache/apt/archives/  
  
ENV HOME /tmp  
ENV AWS_ACCESS_KEY_ID ""  
ENV AWS_SECRET_ACCESS_KEY ""  
VOLUME $HOME/.aws/  
  
COPY backup.sh /usr/bin/backup  
COPY restore.sh /usr/bin/restore  

