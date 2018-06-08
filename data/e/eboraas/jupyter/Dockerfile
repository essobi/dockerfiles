FROM eboraas/debian:stretch  
MAINTAINER Ed Boraas <ed@boraas.ca>  
  
RUN apt-get update && \  
apt-get -y install pkg-config python python-pip && \  
pip install --no-cache-dir --upgrade --ignore-installed pip && \  
for module in $(/usr/local/bin/pip list --no-cache-dir --outdated |cut -f1 -d'
'); do /usr/local/bin/pip install --no-cache-dir --upgrade ${module}; done &&
\  
/usr/local/bin/pip install --no-cache-dir --upgrade ipykernel jupyter && \  
dpkg --purge pkg-config python-pip && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
WORKDIR /mnt/notebooks  
EXPOSE 8888  
CMD ["/bin/sh", "-c", "/usr/local/bin/jupyter-notebook --no-browser
--ip=0.0.0.0 --notebook-dir=/mnt/notebooks"]  
  

