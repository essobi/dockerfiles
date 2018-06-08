# Build from python 3  
FROM python:3  
# Add the pip package list  
ADD ./requirements.txt /tmp/  
ADD ./run_flexget.sh /usr/bin/  
# Setup the environment  
RUN pip install --upgrade -r /tmp/requirements.txt && \  
locale >> /etc/environment && \  
mkdir -p /flexget/config /flexget/mount && \  
useradd -d /flexget -s /bin/bash flexget && \  
chown -R flexget:flexget /flexget && \  
chmod -R 755 /flexget && \  
chmod +x /usr/bin/run_flexget.sh  
EXPOSE 5050  
CMD ["/bin/bash", "/usr/bin/run_flexget.sh"]

