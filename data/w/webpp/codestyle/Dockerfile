FROM ubuntu:16.04  
  
RUN set -x && \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's|archive.ubuntu.com|mirror.yandex.ru|' /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -yq --no-install-recommends \  
python3 python3-pip nodejs npm \  
npm php-pear python3-setuptools && \  
npm install -g jshint jscs jscs-fixer csscomb htmlcs walk brace-expansion && \  
pear install PHP_CodeSniffer && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
rm -rf /var/lib/apt/lists/*  
  
  
COPY . /tmp/codestyle  
  
RUN pip3 install --no-cache-dir --upgrade pip setuptools && \  
cd /tmp/codestyle && python3 setup.py install && \  
rm -rf /tmp/codestyle  
  
ENTRYPOINT ["codestyle"]  

