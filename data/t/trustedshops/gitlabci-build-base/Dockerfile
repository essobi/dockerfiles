FROM centos:7  
WORKDIR /opt  
ENV DOCKER_HOST="\$DOCKER_PORT"  
RUN yum install -y wget git && \  
wget https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && \  
tar -xvf docker-latest.tgz && \  
echo -e "#!/bin/bash\nDOCKER_HOST=\$DOCKER_PORT /opt/docker/docker \$@" >
/usr/bin/docker && \  
chmod u+x /usr/bin/docker  
RUN yum install -y openssh-clients && mkdir -p ~/.ssh && echo -e "Host
*\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  

