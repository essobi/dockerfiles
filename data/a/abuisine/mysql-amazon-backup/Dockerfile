FROM mysql:5.6  
MAINTAINER Alexandre Buisine <alexandrejabuisine@gmail.com>  
LABEL version="1.0.0"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \  
&& apt-get install -yqq \  
duplicity \  
python-boto \  
xtrabackup \  
&& apt-get -yqq clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD resources/*.sh /usr/local/sbin/  
RUN chmod +x /usr/local/sbin/*.sh \  
&& sed -ie '/exec "$@"/ i\  
if [ -d "/restores/mysql" ]; then\n\  
echo\n\  
echo "Restore requested, processing ..."\n\  
rsync -avrP /restores/mysql/ "$DATADIR" && chown -R mysql:mysql "$DATADIR" &&
echo "Done" || echo "Failed"\n\  
echo "Removing restore image ..."\n\  
rm -r /restores/mysql && echo "Done" || echo "Failed"\n\  
echo\n\  
echo "Mysql restore process done. Ready for start up."\n\  
echo\n\  
fi\n\  
' /entrypoint.sh  
  
VOLUME /backups  
VOLUME /restores  
  
ENV PASSPHRASE="" AWS_REGION="" AWS_BUCKET="" AWS_FOLDER=""
AWS_ACCESS_KEY_ID="" AWS_SECRET_ACCESS_KEY=""

