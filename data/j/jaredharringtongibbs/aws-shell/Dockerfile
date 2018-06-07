FROM ubuntu:17.10  
LABEL maintainer="Jared Harrington-Gibbs"  
LABEL description="A docker image that boots to aws-shell"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-
utils python3 groff && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip && \  
pip3 install --upgrade ez_setup && \  
pip3 install --upgrade setuptools && \  
pip3 install --upgrade wheel && \  
pip3 install --upgrade aws-shell && \  
apt-get remove -y --purge apt-utils && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["-c","aws-shell"]  

