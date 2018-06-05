FROM datadog/docker-dd-agent:latest  
  
# There are some values that, although out-commented in the default config,
are needed because of  
# some funky preprocessing done in the dogstats startup scripts.  
# Thus I do this, instead of ADD  
# Install web3  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y gcc python-dev \  
&& /opt/datadog-agent/embedded/bin/pip install web3 \  
&& apt-get remove -y gcc python-dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "service_discovery_backend: docker" >> /etc/dd-agent/datadog.conf  
  
# Add geth collector  
ADD ethereum.py /etc/dd-agent/checks.d/ethereum.py  
#ADD ethereum.yaml /etc/dd-agent/conf.d/ethereum.yaml  

