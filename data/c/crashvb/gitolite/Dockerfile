FROM crashvb/nginx:latest  
MAINTAINER Richard Davis <crashvb@gmail.com>  
  
# Install packages, download files ...  
RUN docker-apt cgi.pm gitolite3 gitweb highlight markdown locales openssl
pandoc patch && \  
git clone git://github.com/kogakure/gitweb-theme.git /usr/share/gitweb-theme
&& \  
rm --force --recursive /usr/share/gitweb-theme/.git  
  
# Configure: gitolite  
ENV GITOLITE_HOME=/var/lib/git  
RUN useradd --comment "Gitolite" \--home=${GITOLITE_HOME} \--shell=/bin/bash
git && \  
sed --in-place '/^umask/s/0077/0027/g' /usr/share/gitolite3/lib/Gitolite/Rc.pm  
  
# Configure: gitweb  
ENV GITWEB_HOME=/usr/share/gitweb GITWEB_THEME=/usr/share/gitweb-theme  
ADD gitweb.cgi.patch ${GITWEB_HOME}/  
ADD gitweb.css.patch ${GITWEB_THEME}/  
ADD gitweb.conf.* /usr/local/share/gitweb/  
RUN usermod --append --groups=git www-data && \  
(cd ${GITWEB_THEME} && ${GITWEB_THEME}/setup --install --verbose) && \  
patch ${GITWEB_HOME}/gitweb.cgi ${GITWEB_HOME}/gitweb.cgi.patch && \  
patch ${GITWEB_THEME}/gitweb.css ${GITWEB_THEME}/gitweb.css.patch && \  
rm ${GITWEB_HOME}/gitweb.cgi.* ${GITWEB_THEME}/gitweb.css.*  
  
# Configure: nginx  
ADD default.nginx /etc/nginx/sites-available/default  
  
# Configure: root  
ADD .gitconfig clone-gitolite-admin /root/  
  
# Configure: sshd  
RUN sed --in-place 's/^AcceptEnv LANG LC_\\*$//g' /etc/ssh/sshd_config && \  
rm --force /etc/ssh/ssh_host_* && \  
mkdir --parents /var/run/sshd  
  
# Configure: supervisor  
ADD supervisord.sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
# Configure: system  
RUN locale-gen en_US.UTF-8 && \  
dpkg-reconfigure --frontend=noninteractive locales  
  
# Configure: entrypoint  
ADD entrypoint.gitolite /etc/entrypoint.d/30gitolite  
ADD entrypoint.gitweb /etc/entrypoint.d/40gitweb  
ADD entrypoint.sshc /etc/entrypoint.d/20sshc  
ADD entrypoint.sshd /etc/entrypoint.d/10sshd  
  
EXPOSE 22/tcp  
  
VOLUME /etc/ssh /root/.ssh ${GITOLITE_HOME}  

