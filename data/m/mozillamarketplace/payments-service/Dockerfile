# For the full stack, see https://github.com/mozilla/payments-env/  
FROM mozillamarketplace/centos-mysql-mkt:latest  
RUN yum install -y supervisor bash-completion && yum clean all  
# This is for the cryptography module:  
RUN yum install -y libffi-devel python-devel openssl-devel && yum clean all  
  
# Copy requirements over first to cache peep install.  
COPY requirements /srv/payments-service/requirements  
  
RUN pip install --find-links https://pyrepo.addons.mozilla.org/ peep  
# TODO: add caching when available. https://github.com/erikrose/peep/issues/93  
RUN peep install \  
\--no-deps -r /srv/payments-service/requirements/dev.txt \  
\--no-deps -r /srv/payments-service/requirements/compiled.txt \  
\--find-links https://pyrepo.addons.mozilla.org/  
  
# Ship the source in the container.  
COPY . /srv/payments-service  
  
EXPOSE 8000  
# Preserve bash history across image updates.  
# This works best when you link your local source code  
# as a volume.  
ENV HISTFILE /srv/payments-service/docker/artifacts/bash_history  
# Configure bash history.  
ENV HISTSIZE 50000  
ENV HISTIGNORE ls:exit:"cd .."  
# This prevents dupes but only in memory for the current session.  
ENV HISTCONTROL erasedups  

