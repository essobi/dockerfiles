FROM fedora:latest  
MAINTAINER Paolo Antinori  
RUN dnf update -y && \  
dnf install -y gcc git python python-pip python-devel python2-enchant gettext
sudo redhat-rpm-config  
  
RUN pip install web.py git+https://github.com/paoloantinori/sopel.git@userserv  
  
ENV _USER=sopel  
ENV _HOME=/home/${_USER}  
RUN useradd -m -d ${_HOME} ${_USER}  
WORKDIR ${_HOME}  
  
COPY scripts/ /tmp/scripts  
COPY start.sh /home/${_USER}  
# this convoluted thing is because of issues to perform `chown` across
multiple commands  
RUN chmod a+rwx ${_HOME} &&\  
rm -rf ${_HOME}/.sopel &&\  
mkdir -p ${_HOME}/.sopel &&\  
cp -R /tmp/scripts/* ${_HOME}/.sopel &&\  
chown -R ${_USER}:${_USER} ${_HOME}/.sopel &&\  
chmod -R a+rwx ${_HOME} &&\  
rm -rf /tmp/scripts  
# VOLUME /home/sopel/.sopel  
USER ${_USER}  
  
CMD ${_HOME}/start.sh  
  
ENV LANG=en_US.UTF-8 \  
IRC_NICK=bot_fuse_maintenance \  
IRC_HOST=irc.devel.redhat.com \  
IRC_PORT=6667 \  
IRC_OWNER=paolo \  
IRC_ADMINS=paolo \  
IRC_CHANS="#fusesustaining" \  
SOPEL_EXTRA=${_HOME}/.sopel/modules \  
EXCLUDE_MODULES=adminchannel,announce,calc,clock,currency,dice,etymology,ip,lmgtfy,ping,rand,reddit,safety,search,tld,unicode_info,units,uptime,url,version,weather,ipython
\  
TWITTER_KEY=key \  
TWITTER_SECRET=secret \  
GH_TOKEN=secret  

