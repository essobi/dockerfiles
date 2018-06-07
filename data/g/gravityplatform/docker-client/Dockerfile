FROM fedora/ssh  
  
EXPOSE 22  
RUN yum install -y \  
docker-io \  
&& echo "Installing docker-machine" \  
&& curl -L https://github.com/docker/machine/releases/download/v0.3.0/docker-
machine_linux-amd64 > /usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine \  
&& echo "Installing docker-compose" \  
&& curl -L https://github.com/docker/compose/releases/download/1.3.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& yum clean all  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  

