# Set the base image to use to Ubuntu  
FROM ubuntu:12.04  
RUN apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget supervisor unzip
ca-certificates  
  
RUN echo 'deb http://repo.acestream.org/ubuntu/ precise main' >
/etc/apt/sources.list.d/acestream.list  
RUN wget -q -O - http://repo.acestream.org/keys/acestream.public.key | apt-key
add -  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y acestream-engine python-
dev gcc  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN adduser --disabled-password --gecos "" tv  
  
RUN cd /tmp/ && wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
  
RUN cd /tmp/ && wget
https://github.com/AndreyPavlenko/aceproxy/archive/master.zip -O master.zip  
RUN cd /tmp/ && unzip master.zip -d /home/tv/  
  
RUN cd /home/tv/aceproxy-master/ && python -m pip install -r requirements.txt
-U  
RUN python -m pip install requests  
  
RUN echo 'root:password' |chpasswd  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 8000  
ENTRYPOINT ["/start.sh"]  

