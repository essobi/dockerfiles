FROM trevorj/ubuntu-salt-minion  
MAINTAINER Trevor Joynson "<docker@trevor.joynson.io>"  
ENV STATE_ROOT=$IMAGE_ROOT/states \  
PILLAR_ROOT=$IMAGE_ROOT/pillar \  
LAYERS_ROOT=$IMAGE_ROOT/layers  
  
WORKDIR $IMAGE_ROOT/pypkgs/salt-layers  
  
COPY setup.* ./  
COPY tools tools  
  
# TODO Figure out pbr static version handling  
COPY .git .git  
  
RUN set -exv \  
#&& lazy-apt-with --no-install-recommends \  
&& lazy-apt --no-install-recommends \  
libgmp-dev build-essential python-dev python-pip python-wheel python-
setuptools git \  
&& :  
  
RUN set -exv \  
&& fake-python-package salt.layers \  
&& pip install -e . \  
&& :  
  
COPY salt_layers salt_layers  

