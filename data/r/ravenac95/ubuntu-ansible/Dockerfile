FROM ubuntu:16.04  
MAINTAINER Reuven Gonzales <reuven@virtru.com>  
  
LABEL packsible.provides="base"  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y git-core python-dev python-pip libffi-dev libssl-dev apt-
transport-https && \  
pip install -U pip && \  
pip install ansible && \  
mkdir -p ~/.ssh && \  
chmod 700 ~/.ssh && \  
echo 'github.com ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=='
>> ~/.ssh/known_hosts  

