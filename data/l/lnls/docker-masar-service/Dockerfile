# Masar server with additional configurations  
FROM lnls/docker-epics-dev:v0.1.2  
MAINTAINER Lucas Russo  
  
# User root user to install software  
USER root  
  
# Install missing dependencies  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
apt-get update && apt-get install -y \  
python2.7-dev \  
python-pip \  
sqlite3 \  
python-qt4 \  
python-pymongo \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install cothread  
  
# Setup git, only for applying patches  
RUN git config --global user.email "masar-service-docker@masar-service-
docker.com"  
RUN git config --global user.name "MASAR_SERVICE Docker"  
  
# Create directories  
RUN mkdir -p /build /var/log/supervisor  
  
# Copy compilation scripts to build directory  
COPY setup.sh \  
env-vars.sh \  
bash.bashrc.local \  
download-install-app.sh \  
/build/  
  
# Copy supervisor config file  
COPY scripts/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Change to build directory  
WORKDIR /build  
  
## Compile application  
RUN echo nameserver 10.0.0.71 >> /etc/resolv.conf && \  
/build/setup.sh  
  
# Create volume for SQLite configuration  
VOLUME /var/lib/sqlite/config  
# Create volume for SQLite data  
VOLUME /var/lib/sqlite/data  
  
# Change to root directory  
WORKDIR /  
  
# Copy another entrypoint for user use  
COPY scripts/docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# Run service  
CMD ["/usr/bin/supervisord"]  

