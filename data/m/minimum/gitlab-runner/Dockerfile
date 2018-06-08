FROM gitlab/gitlab-runner  
  
MAINTAINER Minimum (s5550055@yahoo.com.tw)  
  
ENV TZ=Asia/Taipei  
  
SHELL ["/bin/bash", "-c"]  
  
ENTRYPOINT ["/usr/bin/dumb-init"]  
  
# Install Docker  
RUN \  
apt-get update \  
&& apt-get install -qy --auto-remove curl python3 git \  
&& (curl -s https://bootstrap.pypa.io/get-pip.py | python3) \  
&& (curl -fsSL https://get.docker.com/ | sh) \  
&& pip3 install -U pip docker-compose pyyaml \  
&& apt-get autoremove \  
&& apt-get clean  
  
COPY docker-entrypoint.sh /  
CMD /docker-entrypoint.sh  

