FROM ubuntu:trusty  
  
MAINTAINER Barak Peleg <barak@thumzap.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_US.UTF-8  
##############################################################################  
# Install basic Ubuntu packages  
##############################################################################  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
vim.tiny wget curl sudo net-tools pwgen \  
git-core logrotate software-properties-common && \  
locale-gen en_US en_US.UTF-8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
##############################################################################  
# Install Postgresql  
##############################################################################  
RUN apt-get update && \  
apt-get install -y -q --no-install-recommends \  
postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 postgresql-server-
dev-9.3 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i '1s/^/local all postgres md5\n/' /etc/postgresql/9.3/main/pg_hba.conf
&&\  
echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf && \  
echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf && \  
rm -rf /var/lib/postgresql/9.3/main && \  
update-rc.d -f postgresql disable  
  
RUN mkdir -p /var/run/postgresql/9.3-main.pg_stat_tmp && \  
chown postgres.postgres /var/run/postgresql/9.3-main.pg_stat_tmp -R  
  
VOLUME ["/var/lib/postgresql"]  
  
EXPOSE 5432  
##############################################################################  
# Install Redis  
##############################################################################  
RUN apt-get update && \  
apt-get install --no-install-recommends -y redis-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
update-rc.d -f redis-server disable && \  
sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf  
  
VOLUME ["/var/lib/redis"]  
  
EXPOSE 6379  
##############################################################################  
# Install Ruby  
##############################################################################  
RUN apt-get update && \  
gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && \  
apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV HOME /root  
# See: http://rvm.io/support/faq#i-want-to-install-for-root-only  
RUN echo 'export rvm_prefix="$HOME"' > /root/.rvmrc && \  
echo 'export rvm_path="$HOME/.rvm"' >> /root/.rvmrc  
RUN \curl -ksSL https://get.rvm.io | bash -s stable --ruby  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
ENV PATH
/usr/local/rvm/bin:/usr/local/rvm/rubies/default/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN /bin/bash -l -c "rvm get stable && \  
rvm install 2.2.0 --verify-downloads 1 && \  
rvm use 2.2.0"  
##############################################################################  
# Install SSHD  
##############################################################################  
RUN apt-get update && apt-get install -y openssh-server && \  
mkdir /var/run/sshd && \  
echo 'root:password' | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
##############################################################################  
# Start Services  
##############################################################################  
RUN mkdir -p /usr/local/bin  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
CMD ["/usr/local/bin/run.sh"]  

