#Inspiration 1: DotCloud  
#Inspiration 2: https://github.com/justnidleguy/  
#Inspiration 3: https://bitbucket.org/xcgd/ubuntu4b  
FROM softapps/docker-ubuntubaseimage  
MAINTAINER Arun T K <arun.kalikeri@xxxxxxxx.com>  
  
# User root user to install software  
USER root  
  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.5``.  
# install dependencies as distrib packages when system bindings are required  
# some of them extend the basic odoo requirements for a better "apps"
compatibility  
# most dependencies are distributed as wheel packages at the next step  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
TERM=linux apt-get update && \  
TERM=linux apt-get -yq install \  
adduser \  
ghostscript \  
postgresql-client-9.5 \  
python \  
wkhtmltopdf \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install pip & wheel  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
  
ADD sources/pip-req.txt /opt/sources/pip-req.txt  
  
# use wheels from our public wheelhouse for proper versions of listed packages  
# as described in sourced pip-req.txt  
# these are python dependencies for odoo and "apps" as precompiled wheel
packages  
RUN pip install --upgrade --use-wheel --no-index --pre \  
\--find-links=https://googledrive.com/host/0Bz-lYS0FYZbIMXFWazlnRFpqbFE \  
\--requirement=/opt/sources/pip-req.txt  
  
# Install some deps, lessc and less-plugin-clean-css  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN TERM=linux apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
RUN npm install -g less less-plugin-clean-css \  
&& npm cache clear  
  
# create the odoo user  
RUN adduser --home=/opt/odoo --disabled-password --gecos "" \--shell=/bin/bash
odoo  
  
# ADD sources for the oe components  
# ADD an URI always gives 600 permission with UID:GID 0 => need to chmod
accordingly  
# /!\ carefully select the source archive depending on the version  
ADD http://nightly.odoo.com/9.0/nightly/src/odoo_9.0c.latest.tar.gz
/opt/odoo/odoo.tar.gz  
RUN chown odoo:odoo /opt/odoo/odoo.tar.gz  
  
# changing user is required by openerp which won't start with root  
# makes the container more unlikely to be unwillingly changed in interactive
mode  
USER odoo  
  
RUN /bin/bash -c "mkdir -p
/opt/odoo/{bin,etc,sources/odoo/addons,additional_addons,data}" && \  
cd /opt/odoo/sources/odoo && \  
tar -xvf /opt/odoo/odoo.tar.gz --strip 1 && \  
rm /opt/odoo/odoo.tar.gz  
  
RUN /bin/bash -c "mkdir -p /opt/odoo/var/{run,log,egg-cache,ftp,GeoIP}"  
  
# Execution environment  
USER 0  
ADD sources/odoo.conf /opt/sources/odoo.conf  
WORKDIR /app  
VOLUME ["/opt/odoo/var", "/opt/odoo/etc", "/opt/odoo/additional_addons",
"/opt/odoo/data"]  
# Set the default entrypoint (non overridable) to run when starting the
container  
ENTRYPOINT ["/app/bin/boot"]  
CMD ["help"]  
# Expose the odoo ports (for linked containers)  
EXPOSE 8069 8072  
ADD bin /app/bin/  

