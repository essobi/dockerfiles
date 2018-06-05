#  
# Salt Stack Salt Master Container  
#  
FROM debian:jessie  
MAINTAINER Oliver Tupman <otupman@antillion.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SALT_VERSION=2017.7.0  
ENV SALT_PASSWORD=59r{Y3*912  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
libffi-dev \  
libgit2-dev \  
python-dateutil \  
python-git \  
python-pip \  
sudo \  
\--no-install-recommends  
  
# Add salt stack repository  
RUN curl -sSL
"https://repo.saltstack.com/apt/debian/8/amd64/archive/$SALT_VERSION/SALTSTACK-
GPG-KEY.pub" | sudo apt-key add -  
RUN sudo echo "deb
http://repo.saltstack.com/apt/debian/8/amd64/archive/$SALT_VERSION jessie
main" >> /etc/apt/sources.list.d/saltstack.list  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
libssl-dev \  
python-dev \  
python-m2crypto \  
python-pip \  
python-virtualenv \  
swig \  
virtualenvwrapper \  
unzip  
  
# Install Salt  
RUN apt-get update && apt-get install -y \  
salt-master \  
salt-cloud \  
salt-api \  
\--no-install-recommends  
# Install further dependencies  
RUN pip install apache-libcloud python-simple-hipchat boto dnspython cli53  
  
# Salt API installation (along with SSH)  
RUN apt-get -y install gcc \  
python-dev && \  
pip install pyopenssl \  
cherrypy \  
pyvmomi && \  
salt-call --local tls.create_self_signed_cert && \  
apt-get purge -y gcc && apt-get purge -y python-dev && \  
apt-get autoremove -y  
  
ADD create-user.sh /tmp/create-user.sh  
ADD master.api.conf /tmp/master.api.conf  
  
RUN apt-get install -y openssh-server && \  
mkdir /var/run/sshd && \  
echo "root:$SALT_PASSWORD" |chpasswd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
mkdir -p /etc/salt && \  
cat /tmp/master.api.conf >> /etc/salt/master  
  
RUN /tmp/create-user.sh && \  
echo "Cmnd_Alias SALT_CMDS = /usr/bin/salt, /usr/bin/salt-*,
/usr/local/bin/salt, /usr/local/bin/salt-*" >> /etc/sudoers && \  
echo "remotesalt ALL = NOPASSWD: SALT_CMDS" >> /etc/sudoers  
  
# Volumes  
VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt", \  
"/etc/salt/master.d", "/srv/salt", "/etc/salt/", \  
"/etc/salt/cloud.providers.d", "/etc/salt/cloud.profiles.d"]  
  
# Add Run File  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh && \  
mkdir -p /var/log/salt && \  
touch /var/log/salt/master  
#cp /usr/local/bin/salt* /usr/bin/  
# Ports  
EXPOSE 22 4505 4506 8000  
# Run Command  
CMD "/usr/local/bin/run.sh"  

