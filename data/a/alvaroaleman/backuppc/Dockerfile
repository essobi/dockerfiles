FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TMP_CONFIG /backuppc_initial_config  
ENV TMP_DATA /backuppc_initial_data  
ENV PERSISTENT_CONFIG /etc/backuppc  
ENV PERSISTENT_DATA /var/lib/backuppc  
ENV STARTSCRIPT /usr/local/bin/dockerstart.sh  
ENV RESET_PERMISSIONS true  
  
ADD startscript.sh $STARTSCRIPT  
  
RUN \  
# Install packages \  
apt-get update -y && \  
echo 'backuppc backuppc/reconfigure-webserver multiselect apache2' | debconf-
set-selections && \  
apt-get install -y debconf-utils backuppc supervisor && \  
  
# Configure package config to a temporary folder to be able to restore it when
no config is present  
mkdir -p $TMP_CONFIG $TMP_DATA/.ssh && \  
mv $PERSISTENT_CONFIG/* $TMP_CONFIG && \  
mv $PERSISTENT_DATA/* $TMP_DATA && \  
  
# Disable ssh host key checking per default  
echo "host *" >> $TMP_DATA/.ssh/config && \  
echo " StrictHostKeyChecking no" >> $TMP_DATA/.ssh/config && \  
  
# Disable basic auth for package generated config  
sed -i 's/Auth.*//g' $TMP_CONFIG/apache.conf && \  
sed -i 's/require valid-user//g' $TMP_CONFIG/apache.conf && \  
  
# Display Backuppc on / rather than /backuppc  
sed -i 's/Alias \/backuppc/Alias \//' $TMP_CONFIG/apache.conf && \  
# This is required to load images on /  
sed -i "s/^\$Conf{CgiImageDirURL} =.*/\$Conf{CgiImageDirURL} = '\/image';/g"
$TMP_CONFIG/config.pl && \  
  
# Remove host 'localhost' from package generated config  
sed -i 's/^localhost.*//g' $TMP_CONFIG/hosts && \  
  
# Make startscript executable  
chmod ugo+x $STARTSCRIPT  
  
ADD supervisor.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 80  
VOLUME $PERSISTENT_DATA  
VOLUME $PERSISTENT_CONFIG  
  
cmd $STARTSCRIPT  

