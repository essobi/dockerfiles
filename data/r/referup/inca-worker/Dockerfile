FROM referup/apache:dev  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
inotify-tools \  
moreutils \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD \  
https://raw.githubusercontent.com/GoogleCloudPlatform/compute-image-
packages/legacy/google-startup-scripts/usr/share/google/get_metadata_value \  
/usr/share/google/get_metadata_value  
  
ADD files/etc/default/cloe_run /etc/default/cloe_run  
  
ADD files/usr/local/bin/cloe_run /usr/local/bin/  
ADD files/etc/cloe_run/ /etc/cloe_run/  
RUN \  
chmod -v a+x \  
/usr/local/bin/cloe_run \  
/etc/cloe_run/first-run.d/* \  
/usr/share/google/get_metadata_value  
  
RUN php5dismod -s ALL referup-newrelic  
  
CMD [ "sudo", "-Eu", "www-data", "cloe_run" ]  

