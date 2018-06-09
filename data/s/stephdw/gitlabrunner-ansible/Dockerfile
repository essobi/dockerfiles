FROM gitlab/gitlab-runner  
  
RUN apt-get update && apt-get -y install python && cd /tmp && wget
https://bootstrap.pypa.io/get-pip.py && \  
/usr/bin/python /tmp/get-pip.py && \  
pip install ansible && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
mkdir -p /home/gitlab-runner/.ssh && chown gitlab-runner: /home/gitlab-
runner/.ssh  

