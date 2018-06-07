FROM python:3.6-slim-jessie  
LABEL maintainer="alphakilo"  
LABEL version="0.4"  
LABEL description="Builds the OPNsense Sphinx documentations for local viewing
pleasure"  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y &&
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends\  
make  
RUN pip3 install -U \  
sphinx \  
sphinx_rtd_theme \  
sphinxcontrib-blockdiag \  
sphinxcontrib-nwdiag \  
sphinxcontrib-seqdiag \  
sphinxcontrib-actdiag \  
sphinxcontrib-inheritance \  
blockdiagcontrib-cisco  
CMD /usr/bin/make clean && /usr/bin/make html  
WORKDIR /docs

