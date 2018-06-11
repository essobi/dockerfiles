FROM ubuntu:16.04  
LABEL maintainer="Fernando Díaz"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common && \  
if ! command -v gpg > /dev/null; then \  
apt-get install -y --no-install-recommends \  
gnupg2 dirmngr; \  
fi \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc && rm -rf /usr/share/man \  
&& apt-get clean;  
  
RUN apt-add-repository ppa:ansible/ansible \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ansible sudo systemd curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc && rm -rf /usr/share/man \  
&& apt-get clean  
  
RUN mkdir -p /etc/ansible \  
&& echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts  

