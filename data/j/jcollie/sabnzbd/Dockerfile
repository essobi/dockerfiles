FROM registry.fedoraproject.org/fedora:26  
ENV LANG C.UTF-8  
RUN dnf -y update && \  
rm -rf /usr/share/doc /usr/share/man /var/cache/dnf  
RUN dnf -y install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-
release-26.noarch.rpm \  
http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-
release-26.noarch.rpm && \  
rm -rf /usr/share/doc /usr/share/man /var/cache/dnf  
RUN dnf -y install bind-utils \  
gcc \  
git \  
iproute \  
iputils \  
libffi-devel \  
openssl-devel \  
p7zip \  
par2cmdline \  
python2-pip \  
python2-virtualenv \  
redhat-rpm-config \  
tar \  
traceroute \  
unrar \  
unzip && \  
rm -rf /usr/share/doc /usr/share/man /var/cache/dnf  
RUN /usr/bin/virtualenv-2.7 /opt/sabnzbd  
RUN /opt/sabnzbd/bin/pip install --upgrade pip  
RUN /opt/sabnzbd/bin/pip install --upgrade setuptools  
RUN /opt/sabnzbd/bin/pip install --upgrade cffi \  
Cheetah \  
configobj \  
cryptography \  
enum34 \  
feedparser \  
idna \  
ipaddress \  
ndg-httpsclient \  
Markdown \  
pyasn1 \  
pycparser \  
pyOpenSSL \  
sabyenc \  
setuptools \  
six \  
wsgiref  
RUN git clone \--branch develop https://github.com/sabnzbd/sabnzbd.git
/opt/sabnzbd/src  
RUN mkdir /usenet /opt/sabnzbd/etc /opt/sabnzbd/data /opt/sabnzbd/logs  
  
RUN groupadd -g 5000 media  
RUN useradd -u 5000 -g 5000 -d /opt/sabnzbd -M media  
  
EXPOSE 8080  
ENV PYTHONPATH /opt/sabnzbd/src  
  
VOLUME /usenet  
VOLUME /opt/sabnzbd/etc  
VOLUME /opt/sabnzbd/data  
VOLUME /opt/sabnzbd/logs  
  
USER media  
  
ENTRYPOINT ["/opt/sabnzbd/bin/python", "/opt/sabnzbd/src/SABnzbd.py", "--
config-file=/opt/sabnzbd/etc/sabnzbd.ini", "--browser=0", "--weblogging"]  
  
# Local Variables:  
# indent-tabs-mode: nil  
# End:  

