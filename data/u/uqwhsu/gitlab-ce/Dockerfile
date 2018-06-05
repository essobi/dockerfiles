#################################################################  
# Dockerfile to build a GitLab CE server with Omnibus package  
# Adapted from official GitLab Ubuntu docker image to CentOS 6  
# https://about.gitlab.com/downloads/#centos6  
# https://gitlab.com/gitlab-org/omnibus-gitlab/tree/master/docker  
#################################################################  
  
FROM centos:6  
  
MAINTAINER Will Hsu <uqwhsu@gmail.com>  
  
# Install required packages  
# Not install: git-annex  
RUN yum --exclude=kernel* -y update && \  
yum install -y epel-release && \  
yum -y install policycoreutils openssh-server openssh-clients postfix patch
wget sudo initscripts cronie && \  
sed -i 's|Defaults requiretty|Defaults !requiretty|g' /etc/sudoers && \  
sed -i 's|#PermitRootLogin yes|PermitRootLogin no|g' /etc/ssh/sshd_config && \  
sed -i 's|#Banner none|#Banner none\nUseDNS no\nAllowUsers git\nPrintMotd
no\nPrintLastLog no|g' /etc/ssh/sshd_config && \  
cd /tmp && \  
curl -sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-
ce/script.rpm.sh | bash && \  
yum -y install gitlab-ce && \  
yum clean all && \  
sed -i 's|command |command "echo sysctl"\n# |g'
/opt/gitlab/embedded/cookbooks/gitlab/definitions/sysctl.rb && \  
sed -i '/^external_url/s|external_url |#external_url |g' /etc/gitlab/gitlab.rb
&& \  
sed -i '$a host = `hostname`.strip\nexternal_url "http://#{host}"\neval
ENV["GITLAB_OMNIBUS_CONFIG"].to_s' /etc/gitlab/gitlab.rb && \  
cd /sbin && mv initctl initctl.orig && ln -s /bin/true initctl  
  
WORKDIR /etc  
  
# Copy assets  
COPY assets/ /assets/  
RUN chmod 755 /assets/setup /assets/wrapper /assets/update-permissions  
# Setup SSH  
RUN /assets/setup  
  
# Allow to access embedded tools  
ENV PATH /opt/gitlab/embedded/bin:/opt/gitlab/bin:/assets:$PATH  
  
# Resolve error: TERM environment variable not set.  
ENV TERM xterm  
  
# Expose web & ssh  
EXPOSE 443 80 22  
  
# Define data volumes  
VOLUME ["/etc/gitlab", "/var/opt/gitlab", "/var/log/gitlab"]  
  
# Wrapper to handle signal, trigger runit and reconfigure GitLab  
CMD ["/assets/wrapper"]  
  

