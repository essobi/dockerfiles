# Copyright (c) 2017 Arista Networks, Inc. All rights reserved.  
# Arista Networks, Inc. Confidential and Proprietary.  
FROM aristanetworks/base  
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"  
  
# Install haproxy  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& add-apt-repository ppa:vbernat/haproxy-1.7 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
haproxy \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install confd with kubernetes backend  
RUN wget -nv
https://github.com/jfrabaute/confd/releases/download/v0.15.0-dev-k8s/kube-
confd-0.15.0-dev-k8s -O /usr/bin/confd \  
&& echo "2bfde48f7fb73f6966a90fe5584cd77df92a58a256d505c145e67779815840c0
/usr/bin/confd" \  
| sha256sum --strict --check - \  
&& chmod +x /usr/bin/confd  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--", "confd"]  

