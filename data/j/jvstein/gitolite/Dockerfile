FROM alpine:3.7  
ENV GITOLITE_SRC https://github.com/sitaramc/gitolite.git  
ENV GIT_NOTIFIER_SRC https://github.com/rsmmr/git-notifier.git  
  
# Install dependencies  
# Create "git" user and group for ssh logins  
RUN set -x \  
&& apk add --no-cache git perl perl-json openssh python \  
&& addgroup git \  
&& adduser -D -G git -s /bin/sh -h /var/lib/git git \  
&& passwd -u git  
  
# Tweak openssh configuration  
RUN set -x \  
&& sed -i -E -e "s|^#(HostKey.*/etc/ssh/)(ssh_host_.*_key)|\1keys/\2|" \  
-e "s/^#(PermitRootLogin|PasswordAuthentication|PrintMotd).*$/\1 no/" /etc/ssh/sshd_config  
  
# Volume used to store SSH host keys, generated on first run  
VOLUME /etc/ssh/keys  
  
# Volume used to store all Gitolite data (keys, config and repositories),
initialized on first run  
VOLUME /var/lib/git  
  
# Install from the stable master branch  
RUN git clone $GITOLITE_SRC /opt/gitolite \  
&& /opt/gitolite/install -ln /usr/local/bin \  
&& rm -rf /opt/gitolite/.git  
  
RUN git clone $GIT_NOTIFIER_SRC /opt/git-notifier \  
&& ln -s /opt/git-notifier/git-notifier /usr/local/bin/ \  
&& rm -rf /opt/git-notifier/.git  
  
# Entrypoint responsible for SSH host keys generation, and Gitolite data
initialization  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Expose port 22 to access SSH  
EXPOSE 22  
# Default command is to run the SSH server  
CMD ["sshd"]  

