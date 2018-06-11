FROM debian:wheezy  
MAINTAINER jj  
RUN useradd updater  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install wget
python python-pip -y && \  
apt-get clean autoclean && apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
RUN wget -O - --no-check-certificate https://github.com/httpPrincess/store-
updater/archive/master.tar.gz | tar zxf - && \  
ln -s store-updater-master/ /app  
WORKDIR /app/  
RUN pip install -r /app/requirements.txt && chown -R updater /app/  
USER updater  
CMD /app/print_usage.sh && /app/run.py  

