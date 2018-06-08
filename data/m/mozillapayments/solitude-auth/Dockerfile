# This is designed to be run from fig as part of a  
# Marketplace development environment.  
# NOTE: this is not provided for production usage.  
FROM mozillamarketplace/centos-mysql-mkt:latest  
  
RUN yum install -y supervisor bash-completion && yum clean all  
  
# Copy requirements over first to cache the build.  
COPY requirements /srv/auth/requirements  
  
# Download this securely from pyrepo first.  
RUN pip install --no-deps --find-links https://pyrepo.addons.mozilla.org/ peep  
RUN peep install \  
\--download-cache /tmp/pip/cache \  
\--no-deps \  
-r /srv/auth/requirements/dev.txt \  
\--find-links https://pyrepo.addons.mozilla.org/  
  
# Ship the source in the container, its up to docker-compose to override it  
# if it wants to.  
COPY . /srv/auth  
  
EXPOSE 2603  
# Preserve bash history across image updates.  
# This works best when you link your local source code  
# as a volume.  
ENV HISTFILE /srv/auth/docker/bash_history  
# Configure bash history.  
ENV HISTSIZE 50000  
ENV HISTIGNORE ls:exit:"cd .."  
# This prevents dupes but only in memory for the current session.  
ENV HISTCONTROL erasedups  

