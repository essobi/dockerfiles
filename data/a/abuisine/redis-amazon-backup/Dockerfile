FROM redis:3.0  
MAINTAINER Alexandre Buisine <alexandrejabuisine@gmail.com>  
LABEL version="1.0.0"  
  
RUN echo "deb http://httpredir.debian.org/debian wheezy-backports main" >>
/etc/apt/sources.list  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \  
&& apt-get install -yqq \  
python-pip \  
duplicity=0.6.24-1~bpo70+1 \  
&& apt-get -yqq clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY resources/*.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/*.sh \  
&& pip install boto \  
&& sed -ie '/chown -R redis \\./ i\  
AOF_FILE=/restores/appendonly.aof\n\  
\n\  
if [ -f "$AOF_FILE" ]; then\n\  
echo\n\  
echo "Restore requested, processing ..."\n\  
mv $AOF_FILE /data/ && echo "Done" || echo "Failed"\n\  
echo\n\  
echo "Redis restore process done. Ready for start up."\n\  
echo\n\  
fi\n\  
' /entrypoint.sh  
  
VOLUME /backups  
VOLUME /restores  
  
ENV PASSPHRASE="" AWS_REGION="" AWS_BUCKET="" AWS_FOLDER=""
AWS_ACCESS_KEY_ID="" AWS_SECRET_ACCESS_KEY=""  
CMD ["redis-server", "--appendonly", "yes"]

