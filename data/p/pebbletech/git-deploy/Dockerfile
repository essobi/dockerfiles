FROM debian:jessie  
  
RUN sed -i "s/httpredir.debian/deb.debian/g" /etc/apt/sources.list && \  
apt-get clean && \  
apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \  
duplicity \  
openssh-server \  
git \  
curl \  
jq \  
python-pip \  
python-dev \  
procmail \  
gnupg2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install awscli boto virtualenv && \  
rm -rf /tmp/* /var/tmp/*  
  
RUN useradd -m -d /git -s /usr/bin/git-shell git  
RUN usermod -p $(od -An -N20 -v -w20 -tx1 /dev/urandom | tr -d ' ') git  
  
RUN mkdir -p /var/run/sshd /var/log/git-deploy && \  
chown git /var/run/sshd /var/log/git-deploy  
ADD sshd_config /etc/ssh/sshd_config  
  
RUN mkdir -p /backup_volume  
RUN chown -R git:git /backup_volume  
  
ENV PORT=2222  
ENV PATH=/git/bin:/git/git-shell-commands:/git/git-shell-hooks:/opt/git-
deploy/bin:$PATH  
  
ENV DEPLOY_TIMEOUT_TERM=600s  
ENV DEPLOY_TIMEOUT_KILL=620s  
ENV CAPTURE_OUTPUT=true  
  
RUN echo "Git-Deploy Shell" > /etc/motd  
  
EXPOSE $PORT  
  
WORKDIR /git  
  
ADD bin /opt/git-deploy/bin/  
ADD base-hooks /opt/git-deploy/base-hooks/  
RUN mkdir git-shell-commands && ln -s /opt/git-deploy/bin/* git-shell-
commands/  
RUN mkdir git-shell-hooks && ln -s /opt/git-deploy/base-hooks/* git-shell-
hooks/  
ADD init.sh /init.sh  
RUN chown -R git: /git/  
  
RUN touch /var/log/secure && \  
chown git /var/log/secure  
  
USER git  
  
CMD ["bash","/init.sh"]  

