FROM ubuntu:14.04  
MAINTAINER Vincent Robert <vincent.robert@genezys.net>  
  
# Install required packages  
RUN apt-get install -qy --no-install-recommends \  
openssh-server \  
ca-certificates \  
curl \  
&& curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-
ce/script.deb.sh | bash \  
&& apt-get install -qy --no-install-recommends \  
gitlab-ce=7.10.4~omnibus.1-1  
  
# Manage SSHD through runit  
RUN mkdir -p /opt/gitlab/sv/sshd/supervise \  
&& mkfifo /opt/gitlab/sv/sshd/supervise/ok \  
&& printf "#!/bin/sh\nexec 2>&1\numask 077\nexec /usr/sbin/sshd -D" >
/opt/gitlab/sv/sshd/run \  
&& chmod a+x /opt/gitlab/sv/sshd/run \  
&& ln -s /opt/gitlab/sv/sshd /opt/gitlab/service \  
&& mkdir -p /var/run/sshd  
  
# Expose web & ssh  
EXPOSE 80 22  
  
# Default is to run runit & reconfigure  
CMD sleep 3 && gitlab-ctl reconfigure & /opt/gitlab/embedded/bin/runsvdir-
start  
  

