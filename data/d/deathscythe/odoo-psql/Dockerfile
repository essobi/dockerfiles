FROM ubuntu:16.04  
LABEL maintainer="Luis Triana <luis.triana@jarsa.com.mx>"  
LABEL maintainer="Alejandro H. Pineda <ciinn.mexico@gmail.com>"  
  
RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf \  
&& echo 'APT::Get::allow "true";' >> /etc/apt/apt.conf  
# Install apt-utils wget  
RUN apt-get update \  
&& apt-get install apt-utils \  
language-pack-es wget -y \  
&& locale-gen "en_US.UTF-8" "fr_FR.UTF-8"  
ENV LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" LC_ALL="en_US.UTF-8" \  
PYTHONIOENCODING="UTF-8" TERM="xterm" DEBIAN_FRONTEND="noninteractive"  
# Add postgres repo  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main' >>
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \  
apt-key add -  
  
# Install packages  
RUN apt-get update -q && apt-get upgrade -q && \  
apt-get install --allow-unauthenticated -q \  
aptitude \  
build-essential \  
curl \  
fontconfig \  
gdebi-core \  
git \  
libevent-dev \  
libffi-dev \  
libjpeg-dev \  
libldap2-dev \  
libpq-dev \  
libsasl2-dev \  
libssl-dev \  
libx11-6 \  
libxext6 \  
libxml2-dev \  
libxrender1 \  
libxslt-dev \  
nano \  
node-less \  
nodejs \  
npm \  
openssh-server \  
openssl \  
postgresql-10 \  
postgresql-client-10 \  
postgresql-contrib-10 \  
postgresql-server-dev-10 \  
sudo \  
swig \  
xfonts-75dpi \  
xfonts-base \  
xmlstarlet \  
xsltproc \  
xz-utils \  
#Python Libraries  
python-libxslt1 \  
python-openid \  
python-passlib \  
python-pil \  
python-pip \  
python-psutil \  
python-pychart \  
python-simplejson \  
python-unittest2 \  
python-webdav \  
python-zsi \  
python-dev \  
python-openssl \  
python-pandas \  
python-renderpm \  
python-setuptools  
  
# Install wkhtmltopdf  
WORKDIR /tmp  
RUN curl -o wkhtmltox.tar.xz -SL
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& tar xvf wkhtmltox.tar.xz \  
&& cp wkhtmltox/lib/* /usr/local/lib/ \  
&& cp wkhtmltox/bin/* /usr/local/bin/ \  
&& cp -r wkhtmltox/share/man/man1 /usr/local/share/man/  
  
# Update nodejs and install less  
# RUN npm cache clean -f && npm install -g n && n stable  
RUN ln -s /usr/bin/nodejs /usr/bin/node && npm install -g less less-plugin-
clean-css  
  
# Download and install odoo requirements from
github.com/odoo/odoo/requirements.txt  
# Problemas al actualizar pip a version 10. En espera de un fix  
WORKDIR /tmp  
RUN wget -q https://raw.githubusercontent.com/odoo/odoo/11.0/requirements.txt
&& \  
pip install --upgrade pip==9.0.3 && pip install -r requirements.txt  
  
# Python libraries pip  
RUN pip install gdata \  
ninja2 \  
phonenumbers  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
# Add ODOO user  
RUN adduser --home=/home/odoo-11.0/ --disabled-password --gecos ""
\--shell=/bin/bash odoo  
RUN echo 'root:odoo**' | chpasswd  
RUN echo "odoo ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/user && \  
chmod 0440 /etc/sudoers.d/user  
  
# Create odoo-server.conf  
COPY files/odoo-server.conf /home/odoo-11.0/odoo-server.conf  
RUN chown odoo /home/odoo-11.0/odoo-server.conf && \  
chmod +x /home/odoo-11.0/odoo-server.conf  
  
# Create odoo-server service  
COPY files/odoo-server /etc/init.d/odoo-server  
RUN chown odoo /etc/init.d/odoo-server && \  
chmod +x /etc/init.d/odoo-server  
  
#Install Odoo latest stable 11.0  
WORKDIR /home/odoo-11.0  
RUN git clone -b 11.0 --depth=1 https://github.com/odoo/odoo.git odoo  
RUN chown -R odoo:odoo /home/ && chmod +x /home/odoo-11.0/odoo  
  
USER postgres  
  
# Run Postgres Server  
RUN /etc/init.d/postgresql start && \  
psql --command "CREATE USER odoo WITH SUPERUSER PASSWORD 'odoo';"  
  
USER odoo  
  
# Expose ports for odoo, ssh, and postgres  
EXPOSE 8069 8071 8072 22 5432  
# Start ssh, postgres, odoo-server  
CMD sudo service ssh start && \  
sudo service postgresql start && \  
sudo service odoo-server start && \  
bash  

