FROM rvalyi/buildstep  
  
# Ensure UTF-8 locale  
RUN echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale  
RUN locale-gen en_US.UTF-8 && locale-gen pt_BR.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y libsasl2-dev bzr mercurial libxmlsec1-dev graphviz && \  
apt-get install -y python-cups python-dbus python-openssl python-libxml2 && \  
apt-get install -y python-pip xfonts-base xfonts-75dpi && \  
apt-get install -y python-uno python-genshi python-cairo python-lxml
libreoffice libreoffice-java-common && \  
apt-get clean && \  
mkdir /workspace && \  
mkdir -p /opt/devstep/addons/voodoo  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-
amd64.deb && \  
dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb  
  
RUN cd /workspace && \  
wget https://raw.githubusercontent.com/akretion/voodoo-
image/master/stack/build/build_all && \  
wget https://raw.githubusercontent.com/akretion/voodoo-
image/master/stack/build/buildout.dockerfile.cfg && \  
wget https://raw.githubusercontent.com/akretion/voodoo-
image/master/stack/build/fake_odoo7 && \  
wget https://raw.githubusercontent.com/akretion/voodoo-
image/master/stack/build/fake_odoo8 && \  
wget https://raw.githubusercontent.com/akretion/voodoo-
image/master/stack/build/fake_odoo9 && \  
sh build_all  
  
RUN pip install --upgrade setuptools && \  
rm -rf /build && \  
ln -s /bin/herokuish /build  

