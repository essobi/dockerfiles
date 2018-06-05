FROM alpine:edge  
LABEL maintainer="andre.ilhicas@fiercely.pt"  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk add --update --no-cache \  
bash \  
python-dev \  
py-pip \  
ca-certificates \  
wkhtmltopdf \  
tar \  
wget \  
gcc \  
py-lxml \  
linux-headers \  
postgresql-dev \  
libxml2-dev \  
libxslt-dev \  
musl-dev \  
jpeg-dev \  
zlib-dev \  
openldap-dev\  
nodejs \  
nodejs-npm \  
&& update-ca-certificates  
  
RUN addgroup odoo && adduser odoo -s /bin/sh -D -G odoo \  
&& echo "odoo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& mkdir /opt \  
&& wget https://nightly.odoo.com/10.0/nightly/src/odoo_10.0.20170101.tar.gz \  
&& tar -xzf odoo_10.0.20170101.tar.gz -C /opt \  
&& rm odoo_10.0.20170101.tar.gz \  
&& npm install -g less less-plugin-clean-css\  
&& cd /opt/odoo-10.0-20170101 \  
&& pip install -r requirements.txt \  
&& python setup.py install \  
&& rm -r /opt/odoo-10.0-20170101  
  
# Copy entrypoint script and Odoo configuration file  
COPY entrypoint.sh /  
COPY odoo.conf /etc/odoo/  
RUN chown odoo /etc/odoo/odoo.conf  
  
# Mount /mnt/extra-addons for users addons  
RUN mkdir -p /mnt/extra-addons \  
&& chown -R odoo /mnt/extra-addons  
VOLUME ["/mnt/extra-addons"]  
  
# Expose Odoo services  
EXPOSE 8069 8071  
# Set the default config file  
ENV ODOO_RC /etc/odoo/odoo.conf  
  
# Set default user when running the container  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["odoo"]  

