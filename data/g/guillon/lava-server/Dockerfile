FROM debian:jessie-backports  
  
#  
# Installs lava-server from images.validation.linaro.org repository.  
#  
# Sources at: https://github.com/guilon/lava-server.  
#  
# For LAVA installation documentation, refer to:  
# http://www.linaro.org/  
# https://porter.automotivelinux.org/static/docs/v2/  
# https://porter.automotivelinux.org/static/docs/v2/installing_on_debian.html  
#  
# In order to access the lava-server http service, one may at least  
# bind the port 80, for instance run this image with:  
#  
# $ docker run --name lava-server -d -p 8080:80 guillon/lava-server  
#  
# and browse lava-server at http://localhost:8080.  
#  
# Note that it is important to split the installation of postgresql  
# and lava-server into separate commands and start postgresql before  
# actually installing lava-server which needs a running instance for  
# confiouration.  
#  
# Note that the provided entrypoint.sh will create an initial admin  
# accouint optionally and set the initial password to changeit.  
#  
# Note that in order to avoid an AUFS backend issue with directory  
# permissions on /etc/ssl/private, ssl-cert package must be install in the  
# first layer command such that the first layer has the correct permission.  
# Ref to to https://github.com/docker/docker/issues/783  
# which causes postgresql to fail (https://github.com/chbrandt/docker-
dachs/issues/1).  
#  
# The important VOLUMES for persistent storage are defined at the end  
# of the file.  
#  
MAINTAINER Christophe Guillon <christophe.guillon@st.com>  
  
# Install first dependencies and common services  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y ssl-cert wget expect telnet && \  
apt-get install -y postgresql && \  
apt-get install -y apache2  
  
# Install django (>= 1.8) from backports  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -t jessie-backports -y python-django python-django-tables2  
  
# Setup linaro PPA  
RUN wget -q http://images.validation.linaro.org/production-repo/production-
repo.key.asc && \  
apt-key add production-repo.key.asc && \  
rm production-repo.key.asc && \  
echo "deb http://images.validation.linaro.org/production-repo sid main"
>/etc/apt/sources.list.d/linaro.list  
  
# Install lava tools  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y lava-tool lava-dispatcher lava-coordinator  
  
# Install lava server which needs the postgresql service running  
RUN service postgresql start && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y lava-server && \  
service postgresql stop  
  
# Configure the http server  
RUN a2dissite 000-default && \  
a2ensite lava-server.conf  
  
# Setup persistent volumes points  
VOLUME /var/lib/lava  
VOLUME /var/lib/lava-server  
VOLUME /var/lib/postgresql  
  
# Expose services ports  
EXPOSE 80  
EXPOSE 5432  
EXPOSE 3079  
# Set entrypoint script  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT [ "/entrypoint.sh" ]  

