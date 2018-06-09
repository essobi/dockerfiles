FROM ubuntu:16.04  
LABEL description="Ubuntu with Ansible and TeamCity ServiceMessages Ansible
callback plugin" \  
source="https://github.com/rvadim/ansible-teamcity" \  
maintainer="Vadim Reyder <vadim.reyder@gmail.com>"  
  
ENV DEFAULT_CALLBACK_PLUGIN_PATH=/callback_plugins  
ENV DEFAULT_STDOUT_CALLBACK=teamcity_sm  
  
COPY callback_plugins/teamcity_sm.py /callback_plugins  
COPY docker/requirements.txt /  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends python3 python3-pip libssl-dev python3-setuptools && apt-
get clean  
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.txt  
  
WORKDIR /project/  

