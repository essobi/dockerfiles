FROM python:2.7  
RUN apt-get update && \  
apt-get install -y curl git-core libssl-dev libreadline-dev libbz2-dev python-
dev gettext netcat postgresql-client sudo && \  
rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -r hareau && useradd -r -g hareau -G sudo --uid 1000 hareau  
  
RUN mkdir -p /opt/dev/conf && \  
mkdir -p /opt/dev/src && \  
mkdir -p /opt/dev/venv && \  
chown -R hareau:hareau /opt/dev  
  
USER hareau  
  
ENV PYENV_ROOT /opt/dev/.pyenv  
  
RUN ["/bin/bash", "-c", "curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash"]  
RUN ["/bin/bash", "-c", "/opt/dev/.pyenv/bin/pyenv install --list"]  
RUN ["/bin/bash", "-c", "/opt/dev/.pyenv/bin/pyenv install stackless-2.7.8"]  
  
COPY docker-entrypoint.sh /opt/dev/  
  
ENV PYTHON_EGG_CACHE /opt/dev/venv/.python-eggs  
ENV PYENV_VERSION stackless-2.7.8  
VOLUME ["/opt/dev/venv"]  
  
ENTRYPOINT ["/opt/dev/docker-entrypoint.sh"]  

