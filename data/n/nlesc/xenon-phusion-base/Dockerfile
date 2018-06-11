FROM phusion/baseimage:0.9.22  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
# Enable the OpenSSH server (https://github.com/phusion/baseimage-
docker#enabling_ssh)  
RUN rm -f /etc/service/sshd/down && \  
/etc/my_init.d/00_regen_ssh_host_keys.sh && \  
# When this image is used as ssh client then ignore the known hosts  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
echo "HashKnownHosts no" >> /etc/ssh/ssh_config  
# Create a test user  
RUN /usr/sbin/useradd -p $(openssl passwd javagat) -d /home/xenon -m \--shell
/bin/bash xenon  
WORKDIR /home/xenon  
# add ssh config directory  
COPY .ssh .ssh  
  
RUN chmod 700 .ssh && \  
chmod 600 .ssh/id_rsa .ssh/id_dsa .ssh/id_rsa_pw && \  
chmod 644 .ssh/authorized_keys .ssh/id_rsa.pub .ssh/id_dsa.pub
.ssh/id_rsa_pw.pub && \  
chown -R xenon.xenon .ssh  
# Xenon's filesystem integration tests expect certain directory structure,
create it here:  
RUN mkdir -p filesystem-test-fixture/links && \  
echo "Hello World" > filesystem-test-fixture/links/file0 && \  
touch filesystem-test-fixture/links/file1 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file0 /home/xenon/filesystem-
test-fixture/links/link0 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file1 /home/xenon/filesystem-
test-fixture/links/link1 && \  
ln -s /home/xenon/filesystem-test-fixture/links/file2 /home/xenon/filesystem-
test-fixture/links/link2 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link0 /home/xenon/filesystem-
test-fixture/links/link3 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link2 /home/xenon/filesystem-
test-fixture/links/link4 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link6 /home/xenon/filesystem-
test-fixture/links/link5 && \  
ln -s /home/xenon/filesystem-test-fixture/links/link5 /home/xenon/filesystem-
test-fixture/links/link6 && \  
chown -R xenon.xenon /home/xenon/filesystem-test-fixture  
# Expose the running OpenSSH server  
EXPOSE 22  
  
# Upgrade OS  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# define the test that tells us if the docker container is healthy  
HEALTHCHECK \--interval=1s CMD ssh -i /home/xenon/.ssh/id_rsa xenon@localhost
/bin/true || exit 1  

