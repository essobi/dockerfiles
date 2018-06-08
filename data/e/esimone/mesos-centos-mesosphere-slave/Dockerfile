FROM esimone/mesos-centos-mesosphere-base  
  
ADD https://download.docker.com/linux/centos/docker-ce.repo
/etc/yum.repos.d/docker.repo  
  
RUN rpm --import https://download.docker.com/linux/centos/gpg \  
&& yum install -y docker-ce \  
&& yum --enablerepo=* clean all \  
&& rm -rf /var/cache/yum  
  
EXPOSE 5051  
ENTRYPOINT ["/usr/bin/mesos-init-wrapper", "slave"]  
  
CMD ["--no-systemd_enable_support"]  

