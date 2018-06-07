FROM ez123/ops-base-onb:ubuntu1404  
  
MAINTAINER HighSkillz <webdev@highskillz.com>  
  
# ===========================================================================  
#COPY ../files/.terraformrc /root/  
#COPY ../_web_cache/ /tmp/ops/web.cache  
# ===========================================================================  
# Relying on the default behavior or the FROM image (copy everything to
/tmp/ops)  
# Either we set WORKDIR to /tmp/ops/setup  
# or  
# We set env variables to the full path name  
#  
# Choosing the 2nd option for better control  
# Also, setting up the variables in RUN instead of build-wide, because we just  
# need them for the initial setup  
# ===========================================================================  
# Run ansible to configure this image and then cleanup /tmp/ops  
#  
RUN PLAYBOOK=./setup/playbook.yml \  
REQUIREMENTS=./setup/requirements.yml \  
ansible-playbook-wrapper \  
&& \  
rm -rf \  
"${HOME}/.ansible" \  
"${HOME}/.cache" \  
/tmp/ops \  
;  
  
# ===========================================================================  
# Run ansible to configure this image  
VOLUME [ "/data", "/var/log", "/etc/ansible" ]  
WORKDIR /data  
  
#https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/  
#CMD ["/bin/bash"]  
CMD \  
ansible --version | head -n 1 && \  
terraform --version | head -n 1  

