FROM python  
  
RUN \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
ACCC4CF8 && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" \  
| tee /etc/apt/sources.list.d/pgdg.list \  
&& \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
nano \  
pspg \  
vim \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN pip install --no-cache mycli  
  
ENTRYPOINT [ "mycli" ]  

