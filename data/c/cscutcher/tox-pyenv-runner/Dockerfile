FROM ubuntu:xenial  
MAINTAINER cscutche@cisco.com  
ENV PYENV_ROOT /pyenv/  
ENV PATH
/pyenv/shims:/pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV PYENV_INSTALLER_ROOT /pyenv-installer/  
ENV PYENV_REQUIRED_PYTHON_BASENAME required_python_versions.txt  
ENV PYENV_REQUIRED_PYTHON /pyenv-config/$PYENV_REQUIRED_PYTHON_BASENAME  
  
# Copy pyenv installer  
COPY third-party/pyenv-installer $PYENV_INSTALLER_ROOT  
  
# Install prerequisites  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
gawk \  
git \  
libbz2-dev \  
libffi-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
mercurial \  
openjdk-9-jre-headless \  
python-dev \  
python-openssl \  
python-pip \  
python-tox \  
zlib1g-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Install docker tox which allows tox to discover pyenv pythons  
RUN pip install tox-pyenv  
  
# Run pyenv installer  
RUN $PYENV_INSTALLER_ROOT/bin/pyenv-installer  
  
# Copy file listing required python versions  
COPY required_python_versions.txt $PYENV_REQUIRED_PYTHON  
  
# Install required python versions  
RUN while read line; do \  
pyenv install $line || exit 1 ;\  
done < $PYENV_REQUIRED_PYTHON  
  
# Copy tox wrapper script  
COPY run_tox.sh /bin/run_tox.sh  
  
ENV HOME /pyenv-config/  
  
VOLUME /app  
WORKDIR /app  
ENTRYPOINT ["/bin/run_tox.sh"]  

