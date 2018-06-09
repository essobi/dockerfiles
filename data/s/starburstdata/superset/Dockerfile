FROM ubuntu:16.04  
LABEL maintainer="https://www.starburstdata.com/"  
  
RUN set -xeu && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
build-essential `# required for building the cryptography, a superset
dependecy` \  
libffi-dev `# required for building the cryptography, a superset dependecy` \  
libldap2-dev `# required for building the cryptography, a superset dependecy`
\  
libsasl2-dev `# required for building the cryptography, a superset dependecy`
\  
libssl-dev `# required for building the cryptography, a superset dependecy` \  
`# using python2 as this is documented as currently used by Airbnb @
https://superset.incubator.apache.org/installation.html` \  
python \  
python-dev `# required for building the cryptography, a superset dependecy` \  
python-pkg-resources \  
python-pip \  
python-setuptools `# for pip to work` \  
python-wheel `# for pip not to complain` \  
&& \  
pip install --no-cache-dir \  
gevent==1.2.2 `# needed for gunicorn -k gevent` \  
pyhive[presto]==0.5.1 `# recommended for Presto on
https://superset.incubator.apache.org/installation.html` \  
redis==2.10.6 \  
flask==0.12.4 `# TODO remove, should be pulled by superset; was failing
container startup` \  
SQLAlchemy-Utils'~=0.0,<0.33' `# TODO remove, should be pulled by superset;
was failing webapp startup` \  
superset==0.25.0 \  
&& \  
apt-get remove -y \  
\\*-dev \  
build-essential \  
python-pip \  
python-setuptools \  
python-wheel \  
&& \  
apt-get autoremove -y && \  
apt-get clean && rm -rf "/var/lib/apt/lists/*" && \  
echo OK  
  
COPY ./docker-entrypoint.sh /  
  
RUN set -xeu && \  
useradd --no-log-init --system --user-group superset && \  
install --owner superset --group superset --directory /superset && \  
chmod 0755 /docker-entrypoint.sh && \  
echo OK  
  
ENV \  
GUNICORN_CMD_ARGS=" \  
\--bind 0.0.0.0:8088 \  
\--limit-request-field_size 0 \  
\--limit-request-line 0 \  
\--timeout 120 \  
\--worker-class gevent \  
\--workers 4 \  
" \  
SUPERSET_HOME=/superset  
  
VOLUME /superset  
USER superset  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["gunicorn", "superset:app"]  
# Equivalent of `curl -f http://localhost:8088/health' without pulling
additional dependencies.  
HEALTHCHECK CMD ["python", "-c", "from urllib2 import urlopen;
urlopen('http://localhost:8088/health')"]  
EXPOSE 8088  

