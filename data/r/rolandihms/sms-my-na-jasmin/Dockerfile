FROM debian:jessie  
  
MAINTAINER Jookies LTD <jasmin@jookies.net>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r jasmin && useradd -r -g jasmin jasmin  
  
ENV JASMIN_VERSION 0.9b11  
  
# Install requirements  
RUN apt-get update && apt-get install -y \  
python2.7 \  
python-pip \  
python-dev \  
nfs-common \  
libffi-dev \  
libssl-dev \  
rabbitmq-server \  
redis-server \  
supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Jasmin SMS gateway  
RUN mkdir -p /etc/jasmin/resource \  
/etc/jasmin/store \  
/var/log/jasmin \  
&& chown jasmin:jasmin /etc/jasmin/store \  
/var/log/jasmin \  
&& pip install --pre jasmin=="$JASMIN_VERSION"  
  
# Change binding host for jcli  
RUN sed -i '/\\[jcli\\]/a bind=0.0.0.0' /etc/jasmin/jasmin.cfg  
  
# Mount EFS 1  
#RUN mkdir -p /home/ec2-user/efs #&& mount -t nfs4 -o nfsvers=4.1
fs-f4975b3d.efs.eu-west-1.amazonaws.com:/ /home/ec2-user/efs  
# copy in a config file  
COPY jasmin.cfg /etc/jasmin/  
  
# copy in the configs  
COPY /etc/jasmin/store/* /etc/jasmin/store/  
  
EXPOSE 2775 8990 1401  
#VOLUME ["/home/ec2-user/efs/var/log/jasmin:/var/log/jasmin",
"/home/ec2-user/efs/etc/jasmin:/etc/jasmin",
"/home/ec2-user/efs/etc/jasmin/store:/etc/jasmin/store"]  
VOLUME ["/var/log/jasmin:/var/log/jasmin", "/etc/jasmin:/etc/jasmin",
"/etc/jasmin/store:/etc/jasmin/store"]  
#VOLUME ["/var/log/jasmin", "/etc/jasmin", "/etc/jasmin/store"]  
COPY docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
#RUN RESt API Jasmin  
RUN sudo systemctl start jasmin-restapi  
CMD ["jasmind.py", "--enable-interceptor-client", "-u", "jcliadmin", "-p",
"jclipwd"]  

