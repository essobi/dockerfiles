# adapted from [ williamyeh/ansible:ubuntu14.04-onbuild ]  
# "ONBUILD version" because:  
# - updates some SSL stuff everytime is used in another image  
# - copies . to /tmp/ops  
#  
# added some improvements from [ https://github.com/timhaak/docker-base ]  
FROM ez123/ops-base:ubuntu1404  
  
MAINTAINER HighSkillz <webdev@highskillz.com>  
  
RUN \  
echo "===> Initial packages update" && \  
apt-get update && \  
\  
echo "===> Updating TLS certificates..." && \  
apt-get -y install \  
ca-certificates \  
openssl \  
ssl-cert \  
&& \  
\  
\  
echo "===> Cleaning up ..." && \  
apt-get autoremove --purge -y && \  
apt-get clean -y && \  
rm -rf \  
"${HOME}/.cache" \  
/var/cache/apk/* \  
/var/lib/apt/lists/* \  
&& \  
\  
echo "===> Adding hosts for convenience..." && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts && \  
\  
echo "OK!"  
  
ENV TERM="xterm"  
COPY ansible-playbook-wrapper /usr/local/bin/  
  
ONBUILD RUN \  
apt-get update && \  
echo "===> Updating TLS certificates..." && \  
apt-get -y install \  
ca-certificates \  
openssl \  
ssl-cert \  
;  
  
ONBUILD COPY . /tmp/ops  
ONBUILD WORKDIR /tmp/ops  
ONBUILD RUN \  
echo "===> Diagnosis: host information..." && \  
ansible -c local -m setup all  
  
# default command: display Ansible version  
CMD \  
ansible-playbook --version | head -n 1  

