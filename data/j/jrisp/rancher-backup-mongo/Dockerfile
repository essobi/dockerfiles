FROM mongo:latest  
MAINTAINER Sebastien LANGOUREAUX <linuxworkgroup@hotmail.com>  
  
# Add python and cron to manage backup  
RUN apt-get update && \  
apt-get install -y curl python vim python-pip duplicity ncftp python-paramiko
python-gobject-2 python-boto  
  
# Install rancher api for Python  
RUN pip install rancher_metadata  
  
# Install go-cron  
RUN curl -sL https://github.com/michaloo/go-cron/releases/download/v0.0.2/go-
cron.tar.gz \  
| tar -x -C /usr/local/bin  
  
COPY assets/init.py /app/init.py  
COPY assets/run /app/run  
RUN chmod +x /app/run  
  
# CLEAN APT  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/backup/mongo"]  
CMD ["/app/run"]  

