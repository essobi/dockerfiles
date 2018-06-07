FROM insecurity/node:6.4.0  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set variables (Choose version in https://github.com/gilbitron/Raneto/tags,
default master)  
ARG RANETO_VERSION=master  
ARG PORT=3000  
ENV RANETO_INSTALL_DIR /srv/raneto  
  
# Install build dependencies (curl)  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get install -y --no-install-recommends curl \  
# Get last raneto version (master) from sources \  
&& cd /tmp \  
&& curl -SLO
"https://github.com/gilbitron/Raneto/archive/$RANETO_VERSION.tar.gz" \  
&& mkdir -p $RANETO_INSTALL_DIR \  
&& tar -xzf "$RANETO_VERSION.tar.gz" -C $RANETO_INSTALL_DIR --strip-
components=1 \  
&& rm "$RANETO_VERSION.tar.gz" \  
# Install gulp to manage Raneto dependencies \  
&& cd $RANETO_INSTALL_DIR \  
&& npm install --global gulp \  
# Update configuration \  
&& mkdir conf && mkdir custom-template \  
&& sed -i -e "s#\\(./config.default.js\\)#../conf/config.default.js#"
example/server.js \  
&& sed -i -e "s#\\(/content/\\)#/../example/content/#"
example/config.default.js \  
&& cp $RANETO_INSTALL_DIR/example/config.default.js
$RANETO_INSTALL_DIR/conf/config.default.js \  
# Install Raneto \  
&& npm install --production \  
&& gulp \  
# Security - Create and Fix UID/GID of non-root raneto user \  
&& groupadd -g 1000 raneto && useradd -u 1000 -g 1000 raneto \  
&& chown -R raneto:raneto $RANETO_INSTALL_DIR \  
# Create entrypoint script \  
&& echo '#!/bin/bash' > /usr/local/bin/run.sh \  
&& echo "set -o errexit" >> /usr/local/bin/run.sh \  
&& echo "chown -R raneto:raneto $RANETO_INSTALL_DIR" >> /usr/local/bin/run.sh
\  
&& echo "cp -n $RANETO_INSTALL_DIR/example/config.default.js
$RANETO_INSTALL_DIR/conf/config.default.js" >> /usr/local/bin/run.sh \  
&& echo "cp -nR $RANETO_INSTALL_DIR/themes/default
$RANETO_INSTALL_DIR/themes/custom" >> /usr/local/bin/run.sh \  
&& echo "npm start" >> /usr/local/bin/run.sh \  
&& chmod +x /usr/local/bin/run.sh \  
&& chown raneto:raneto /usr/local/bin/run.sh \  
# APT Clean-up \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Let's go  
WORKDIR $RANETO_INSTALL_DIR  
  
EXPOSE $PORT  
  
ENTRYPOINT ["/usr/local/bin/run.sh"]  

