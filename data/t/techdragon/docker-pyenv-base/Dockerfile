FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends curl ca-certificates && \  
apt-get install -y \--no-install-recommends git-core && \  
apt-get install -y \--no-install-recommends mercurial && \  
apt-get install -y \--no-install-recommends build-essential && \  
apt-get install -y \--no-install-recommends libssl-dev && \  
apt-get install -y \--no-install-recommends libreadline-dev && \  
apt-get install -y \--no-install-recommends libbz2-dev && \  
apt-get install -y \--no-install-recommends libsqlite3-dev && \  
apt-get install -y \--no-install-recommends libffi-dev && \  
apt-get install -y \--no-install-recommends python-dev  
  
# apt-get build-dep -n --no-install-recommends python2.7 && \  
# apt-get build-dep -n --no-install-recommends python3.4  
  
ADD profile.bash /root/.bash_profile  
RUN ["/bin/bash", "-c", "curl -k -L
https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-
installer | bash"]  
# RUN ["/bin/bash", "-c", "echo \"export PYENV_ROOT=\"$HOME/.pyenv\"\" >>
/root/.bash_profile"]  
# RUN ["/bin/bash", "-c", "echo \"export
PATH=\"$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH\"\" >> /root/.bash_profile"]  
# RUN ["/bin/bash", "-c", "echo 'eval "$(pyenv init -)"' >>
/root/.bash_profile"]  
# RUN ["/bin/bash", "-c", "echo 'eval "$(pyenv virtualenv-init -)"' >>
/root/.bash_profile"]  
RUN ["/bin/bash", "-c", "/root/.pyenv/bin/pyenv update"]  
RUN ["/bin/bash", "-c", "pyenv install --list"]  
  
# RUN ["/bin/bash", "-c", "/root/.pyenv/bin/pyenv install --list"]  
  
# RUN ["/bin/bash", "-c", "/root/.pyenv/bin/pyenv install 2.7.9"]  
# RUN ["/bin/bash", "-c", "/root/.pyenv/bin/pyenv install 3.4.3"]  
  
  
# RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# RUN apt-get clean  
# RUN apt-get purge  
  
## RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02docker-force-unsafe-io  
## RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/docker-no-
httpcache  
## RUN echo 'Acquire::Languages "none";' > /etc/apt/apt.conf.d/docker-no-
languages  
## RUN echo 'DPkg::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb
/var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >
/etc/apt/apt.conf.d/docker-clean  
## RUN echo 'APT::Update::Post-Invoke { "rm -f /var/cache/apt/archives/*.deb
/var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true"; };' >>
/etc/apt/apt.conf.d/docker-clean  
## RUN echo 'Dir::Cache::pkgcache ""; Dir::Cache::srcpkgcache "";' >>
/etc/apt/apt.conf.d/docker-clean  
## RUN echo 'Acquire::GzipIndexes "true"; Acquire::CompressionTypes::Order::
"gz";' > /etc/apt/apt.conf.d/docker-gzip-indexes  
  
# RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
# ENV PYTHONDONTWRITEBYTECODE true  
  
  
  

