FROM debian:wheezy  
MAINTAINER jj  
RUN useradd killer  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\  
apt-get install python python-pip wget -y && \  
apt-get clean autoclean && apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
RUN wget -O - --no-check-certificate https://github.com/httpPrincess/instance-
killer/archive/master.tar.gz | tar zxf - && \  
ln -s instance-killer-master/ /app  
WORKDIR /app/  
RUN pip install -r /app/requirements.txt && chown -R killer /app/  
USER killer  
CMD /app/print_usage.sh && /app/run.py  

