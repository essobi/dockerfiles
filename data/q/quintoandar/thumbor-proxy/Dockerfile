FROM nginx:1.13.3  
  
RUN apt-get update && apt-get -yqq --no-install-recommends install \  
ca-certificates \  
procps \  
python-pip \  
python-setuptools && \  
pip install newrelic-plugin-agent newrelic-plugin-agent[nginx] && \  
mkdir -p /var/log/newrelic && \  
mkdir -p /var/run/newrelic && \  
apt-get purge -y python-pip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
ADD docker-entrypoint.sh .  
ADD newrelic-plugin-agent.cfg /etc/newrelic/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

