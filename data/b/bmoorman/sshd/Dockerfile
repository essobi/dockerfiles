FROM bmoorman/ubuntu:xenial  
  
ENV SSHD_USERS="docker" \  
SSHD_KEY_LOC="https://raw.githubusercontent.com/iVirus/Docker/master/SSHd/keys"  
  
ARG DEBIAN_FRONTEND="noninteractive"  
  
RUN apt-get update \  
&& apt-get install --yes \--no-install-recommends \  
curl \  
denyhosts \  
iputils-ping \  
openssh-server \  
python-setuptools \  
&& sed --in-place --regexp-extended \  
\--expression 's/^(IPTABLES\s+=\s+.*)/#\1/' \  
\--expression 's/^(ADMIN_EMAIL\s+=\s+.*)/#\1/' \  
\--expression 's/^#(USERDEF_FAILED_ENTRY_REGEX\s*=\s*).*/\1Failed
(?P<method>\\\S*) for (?P<invalid>invalid user |illegal user )?(?P<user>.*)
from (::ffff:)?(?P<host>\\\d{1,3}\\\\.\\\d{1,3}\\\\.\\\d{1,3}\\\\.\\\d{1,3})(
port \\\d+)?( ssh2)?/' \  
/etc/denyhosts.conf \  
&& sed --in-place --regexp-extended \  
\--expression 's/^#(PasswordAuthentication\s+).*/\1no/' \  
/etc/ssh/sshd_config \  
&& easy_install speedtest-cli \  
&& apt-get autoremove --yes \--purge \  
&& apt-get clean \  
&& rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY sshd/ /etc/sshd/  
  
VOLUME /config  
  
EXPOSE 22  
  
CMD ["/etc/sshd/start.sh"]  

