FROM python:2  
ARG APT_PROXY  
RUN set -x && [ -z "$APT_PROXY" ] || /bin/echo -e "Acquire::HTTP::Proxy
\"$APT_PROXY\";\nAcquire::HTTPS::Proxy
\"$APT_PROXY\";\nAcquire::http::Pipeline-Depth \"23\";" >
/etc/apt/apt.conf.d/01proxy  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN set -x \  
&& apt-get -q update \  
&& apt-get -qqy install ca-certificates curl g++ libgpgme11-dev libgpgme11 \  
&& apt-get -qqy autoclean \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd dropbox \  
&& useradd -m -d /dbox -c "Dropbox Daemon Account" -s /usr/sbin/nologin -g
dropbox dropbox \  
&& curl -sL 'https://www.dropbox.com/download?dl=packages/dropbox.py' -o
/usr/bin/dropbox \  
&& chmod +x /usr/bin/dropbox \  
&& pip install pygpgme \  
&& apt-get -y --purge autoremove g++ libgpgme11-dev \  
&& rm -rf /tmp/* /var/tmp/*  
  
ENV HOME /dbox  
  
# Dropbox is weird: it insists on downloading its binaries itself via 'dropbox  
# start -i'. So we switch to 'dropbox' user temporarily and let it do its
thing.  
USER dropbox  
RUN mkdir -p /dbox/.dropbox /dbox/.dropbox-dist /dbox/Dropbox /dbox/base \  
&& echo y | dropbox start -i  
  
# Switch back to root, since the run script needs root privs to chmod to the
user's preferrred UID  
USER root  
  
# Dropbox has the nasty tendency to update itself without asking. In the
processs it fills the  
# file system over time with rather large files written to /dbox and /tmp. The
auto-update routine  
# also tries to restart the dockerd process (PID 1) which causes the container
to be terminated.  
RUN mkdir -p /opt/dropbox \  
# Prevent dropbox to overwrite its binary  
&& mv /dbox/.dropbox-dist/dropbox-lnx* /opt/dropbox/ \  
&& mv /dbox/.dropbox-dist/dropboxd /opt/dropbox/ \  
&& mv /dbox/.dropbox-dist/VERSION /opt/dropbox/ \  
&& rm -rf /dbox/.dropbox-dist \  
&& install -dm0 /dbox/.dropbox-dist \  
# Prevent dropbox to write update files  
&& chmod u-w /dbox \  
&& chmod o-w /tmp \  
&& chmod g-w /tmp \  
# Prepare for command line wrapper  
&& mv /usr/bin/dropbox /usr/bin/dropbox-cli  
  
# Install init script and dropbox command line wrapper  
COPY run /root/  
COPY dropbox /usr/bin/dropbox  
  
WORKDIR /dbox/Dropbox  
EXPOSE 17500  
VOLUME ["/dbox/.dropbox", "/dbox/Dropbox"]  
ENTRYPOINT ["/root/run"]  

