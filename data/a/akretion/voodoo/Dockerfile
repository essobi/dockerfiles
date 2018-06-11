FROM ubuntu:16.04  
USER root  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y libsasl2-dev bzr mercurial libxmlsec1-dev \  
python-pip graphviz xfonts-base xfonts-75dpi npm git \  
wget libpq-dev libjpeg8-dev libldap2-dev locales \  
libffi-dev vim telnet ghostscript poppler-utils && \  
npm install -g less less-plugin-clean-css && \  
ln -sf /usr/bin/nodejs /usr/bin/node && \  
apt-get clean  
  
# Install postgresql client 10  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y postgresql-client-10 && \  
apt-get clean  
  
# Force to install the version 0.12.1 of wkhtmltopdf as recomended by odoo  
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb && \  
dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb  
  
RUN locale-gen pt_BR.UTF-8 && \  
locale-gen en_US.UTF-8 && \  
update-locale LANG=en_US.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
#Install fonts  
ADD stack/fonts/c39hrp24dhtt.ttf /usr/share/fonts/c39hrp24dhtt.ttf  
RUN chmod a+r /usr/share/fonts/c39hrp24dhtt.ttf && fc-cache -f -v  
  
RUN mkdir -p /workspace  
  
# Pre-build environement for odoo  
ADD stack/build /workspace/  
RUN sh /workspace/build  
  
RUN adduser odoo  
  
RUN pip install --upgrade pip && \  
pip install flake8 && \  
pip install pgcli && \  
pip install git+https://github.com/oca/pylint-odoo.git && \  
pip install git+https://github.com/akretion/ak.git@1.4.0  
  
WORKDIR /workspace  
  
COPY stack/entrypoint /usr/local/bin/entrypoint  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
EXPOSE 8069  
USER odoo  
RUN git config --global user.email "voodoo@fake.com" &&\  
git config --global user.name "Voodoo"  

