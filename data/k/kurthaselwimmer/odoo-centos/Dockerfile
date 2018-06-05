FROM centos:7  
MAINTAINER "Bart Bania" <contact@bartbania.com>  
  
COPY ./odoo.repo /etc/yum.repos.d/odoo.repo  
  
RUN set -x; \  
yum clean all \  
&& yum update -y \  
&& yum install -y epel-release \  
&& yum -y install python-pip \  
&& yum install -y ca-certificates \  
curl \  
wget \  
xorg-x11-fonts-75dpi \  
xorg-x11-fonts-Type1 \  
nodejs \  
npm \  
git  
RUN set -x; \  
rpm -ivhU http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-2.noarch.rpm  
RUN set -x; \  
yum install -y postgresql94.x86_64  
  
RUN set -x; \  
yum install -y fontconfig libpng libX11 libXext libXrender xorg-x11-fonts-
Type1 xorg-x11-fonts-75dpi  
  
RUN yum localinstall -y
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
centos7-amd64.rpm  
  
RUN set -x; \  
yum install -y odoo  
  
COPY ./entrypoint.sh /  
COPY ./openerp-server.conf /etc/odoo/  
RUN chown odoo /etc/odoo/openerp-server.conf  
  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons  
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]  
  
EXPOSE 8069 8071  
ENV OPENERP_SERVER /etc/odoo/openerp-server.conf  
  
USER odoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["openerp-server"]  

