FROM ubuntu:16.04  
MAINTAINER Elico Corp <webmaster@elico-corp.com>  
  
# Define build constants  
ENV GIT_BRANCH=9.0 \  
PYTHON_BIN=python \  
SERVICE_BIN=openerp-server  
  
# Set timezone to UTC  
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime  
  
# Generate locales  
RUN apt update \  
&& apt -yq install locales \  
&& locale-gen en_US.UTF-8 \  
&& update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
  
# Install APT dependencies  
ADD sources/apt.txt /opt/sources/apt.txt  
RUN apt update \  
&& awk '! /^ *(#|$)/' /opt/sources/apt.txt | xargs -r apt install -yq  
  
# Create the odoo user  
RUN useradd --create-home --home-dir /opt/odoo --no-log-init odoo  
  
# Switch to user odoo to create the folders mapped with volumes, else the  
# corresponding folders will be created by root on the host  
USER odoo  
  
# If the folders are created with "RUN mkdir" command, they will belong to
root  
# instead of odoo! Hence the "RUN /bin/bash -c" trick.  
RUN /bin/bash -c "mkdir -p
/opt/odoo/{etc,sources/odoo,additional_addons,data,ssh}"  
  
# Add Odoo sources and remove .git folder in order to reduce image size  
WORKDIR /opt/odoo/sources  
RUN git clone https://github.com/odoo/odoo.git -b $GIT_BRANCH \  
&& rm -rf odoo/.git  
  
ADD sources/odoo.conf /opt/odoo/etc/odoo.conf  
ADD auto_addons /opt/odoo/auto_addons  
  
User 0  
# Install Odoo python dependencies  
RUN pip install -r /opt/odoo/sources/odoo/requirements.txt  
  
# Install extra python dependencies  
ADD sources/pip.txt /opt/sources/pip.txt  
RUN pip install -r /opt/sources/pip.txt  
  
# Install LESS  
RUN npm install -g less@2.7.3 less-plugin-clean-css@1.5.1 \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install wkhtmltopdf based on QT5  
# Warning: do not use latest version (0.12.2.1) because it causes the footer  
# issue (see https://github.com/odoo/odoo/issues/4806)  
ADD
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-
trusty-amd64.deb \  
/opt/sources/wkhtmltox.deb  
RUN dpkg -i /opt/sources/wkhtmltox.deb  
  
# Startup script for custom setup  
ADD sources/startup.sh /opt/scripts/startup.sh  
  
# Provide read/write access to odoo group (for host user mapping). This
command  
# must run before creating the volumes since they become readonly until the  
# container is started.  
RUN chmod -R 775 /opt/odoo && chown -R odoo:odoo /opt/odoo  
  
VOLUME [ \  
"/opt/odoo/etc", \  
"/opt/odoo/additional_addons", \  
"/opt/odoo/data", \  
"/opt/odoo/ssh", \  
"/opt/scripts" \  
]  
  
# Use README for the help & man commands  
ADD README.md /usr/share/man/man.txt  
# Remove anchors and links to anchors to improve readability  
RUN sed -i '/^<a name=/ d' /usr/share/man/man.txt  
RUN sed -i -e 's/\\[\^\\]\\[toc\\]//g' /usr/share/man/man.txt  
RUN sed -i -e 's/\\(\\[.*\\]\\)(#.*)/\1/g' /usr/share/man/man.txt  
# For help command, only keep the "Usage" section  
RUN from=$( awk '/^## Usage/{ print NR; exit }' /usr/share/man/man.txt ) && \  
from=$(expr $from \+ 1) && \  
to=$( awk '/^ \$ docker-compose up/{ print NR; exit }' /usr/share/man/man.txt
) && \  
head -n $to /usr/share/man/man.txt | \  
tail -n +$from | \  
tee /usr/share/man/help.txt > /dev/null  
  
# Use dumb-init as init system to launch the boot script  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb /opt/sources/dumb-init.deb  
RUN dpkg -i /opt/sources/dumb-init.deb  
ADD bin/boot /usr/bin/boot  
ENTRYPOINT [ "/usr/bin/dumb-init", "/usr/bin/boot" ]  
CMD [ "help" ]  
  
# Expose the odoo ports (for linked containers)  
EXPOSE 8069 8072  

