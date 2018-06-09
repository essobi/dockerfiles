#  
# Outils de construction de style et des données SQLite de strass  
#  
  
FROM bersace/strass-runtime  
  
RUN set -x; \  
apt-get update -y; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
faketime \  
git \  
make \  
openssh-client \  
phpunit \  
python3-dev \  
python3-pip \  
sqlite3 \  
; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
pip3 install --upgrade pip setuptools wheel; \  
pip install --no-cache-dir --upgrade libsass pytest pyyaml selenium webassets;
\  
rm -rf ~/.cache/; \  
:  

