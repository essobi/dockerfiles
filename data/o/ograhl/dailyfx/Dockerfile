FROM ograhl/job:latest  
  
  
### ENV Variablen  
ENV \  
CURRENCIES="USD,GBP" \  
XML_URL="http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" \  
MY_SCREEN_NAME="please_set_environment_variable" \  
MY_LANGUAGE="en" \  
CONSUMER_KEY="please_set_environment_variable" \  
CONSUMER_SECRET="please_set_environment_variable" \  
ACCESS_TOKEN="please_set_environment_variable" \  
ACCESS_TOKEN_SECRET="please_set_environment_variable"  
# APT-GET Installs  
RUN \  
apt-get update && \  
\  
echo "Installing Tools..." && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
bc \  
ca-certificates \  
curl \  
jq \  
nkf \  
openssl \  
vim \  
wget \  
&& \  
\  
echo "Cleaning up..." && \  
rm -r /var/lib/apt/lists/*  
  
  
### Kopiere Dateien  
# Skripte nach /  
COPY scripts/*.sh /  
  
  
### Finale RUN-Schritte  
# - Skripte ausführbar machen  
RUN \  
echo "Make scripts executable..." && \  
chmod 744 /*.sh && \  
\  
echo "Create directories..." && \  
mkdir -p /var/rates  
  
  
### Volumes  
VOLUME /var/rates  
  

