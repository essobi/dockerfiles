FROM gitlab/gitlab-runner:ubuntu-v10.8.0  
ADD https://github.com/JonasProgrammer/docker-machine-driver-
hetzner/releases/download/1.2.0/docker-machine-driver-
hetzner_1.2.0_linux_amd64.tar.gz /tmp/docker-machine-driver-hetzner.tar.gz  
RUN cd /tmp && \  
tar xvfz docker-machine-driver-hetzner.tar.gz && \  
chmod +x docker-machine-driver-hetzner && \  
mv docker-machine-driver-hetzner /usr/local/bin/ && \  
rm -f /tmp/docker-machine-driver-hetzner.tar.gz  

