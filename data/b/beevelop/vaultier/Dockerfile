FROM beevelop/base  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
WORKDIR /opt/vaultier  
  
COPY vaultier_conf.py start.sh ./  
  
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/lib/python2.7/dist-packages/vaultier"  
  
RUN mkdir -p /opt/vaultier/logs /opt/vaultier/media /opt/vaultier/data/static
&& \  
apt-get -qq update && \  
apt-get -qq install python python-dev python-pip libpq-dev gcc -y && \  
apt-get -qq install curl git ssh -y && \  
  
easy_install --upgrade pip && \  
pip install vaultier==0.7.5 && \  
  
pip install South==1.0.2 && \  
sed -i -e 's/South==0\.8\.4/South==1\.0\.2/g' /usr/local/lib/python2.7/dist-
packages/Vaultier-0.7.5.egg-info/requires.txt && \  
  
pip install six==1.9 && \  
sed -i -e 's/six==1\.4\.1/six==1\.9/g' /usr/local/lib/python2.7/dist-
packages/Vaultier-0.7.5.egg-info/requires.txt && \  
  
pip install requests==2.6.0 && \  
sed -i -e 's/requests==2\.3\.0/requests==2\.6\.0/g'
/usr/local/lib/python2.7/dist-packages/Vaultier-0.7.5.egg-info/requires.txt &&
\  
  
vaultier collectstatic --noinput  
  
VOLUME ["/opt/vaultier/logs", "/opt/vaultier/data"]  
  
CMD ["./start.sh"]  
  
EXPOSE 80  

