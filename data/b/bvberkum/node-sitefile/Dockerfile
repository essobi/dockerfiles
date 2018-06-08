ARG DCKR_TAG=dev  
FROM bvberkum/treebox:$DCKR_TAG  
MAINTAINER B. van Berkum <dev@dotmpe.com>  
  
  
ARG sf_checkout=dev  
  
ADD sudoers-treebox /etc/sudoers.d/treebox-2  
RUN cat /etc/sudoers.d/* || true  
ARG username=treebox  
  
USER root  
  
# Prepare for Sitefile  
RUN \  
mkdir -vp /home/$username /opt/bvberkum /src/github.com/bvberkum && \  
chmod -R g+rw /usr/local/* /usr/local/lib/node_modules /opt/bvberkum
/src/github.com/bvberkum && \  
chgrp -R staff /usr/local/* /usr/local/lib/node_modules /opt/bvberkum
/src/github.com/bvberkum && \  
chown -R $username:$username /home/$username /opt/bvberkum  
  
USER $username  
  
# Set LTS and get SASS and SQLite build  
RUN n lts && npm install -g node-sass@4.0.0 sqlite3@3.1.8 coffee-script@1.12.2  
  
# Checkout Sitefile  
RUN USER=$username && \  
git clone https://github.com/bvberkum/node-sitefile.git /opt/bvberkum/node-
sitefile && \  
cd /opt/bvberkum/node-sitefile && \  
git checkout $sf_checkout  
  
# Install Sitefile  
RUN USER=$username && \  
npm install -g grunt coffee-script && \  
cd /opt/bvberkum/node-sitefile && \  
npm install --quiet . && \  
npm install --quiet -g .  
  
RUN sudo rm /etc/sudoers.d/$username  
  
ENV site_src=github.com/bvberkum/node-sitefile  
ENV site_repo=  
ENV site_version=  
  
RUN mkdir -vp /usr/local/share/sitefile  
COPY ./entry.sh /usr/local/share/sitefile/entry.sh  
ENTRYPOINT ["/usr/local/share/sitefile/entry.sh"]  
EXPOSE 7000-7099  
CMD ["","",""]  
  
# Id: sitefile/0.0.7-dev  

