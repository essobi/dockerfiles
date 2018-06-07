FROM debian:jessie  
  
RUN \  
apt-get update && apt-get -y upgrade && \  
apt-get install -y openssh-server && \  
rm -rf /var/lib/apt/lists/*  
  
# Prepare sftp only part  
RUN addgroup --gid 30100 sftponly  
  
# Use an impossible password. In some environments 'usePAM=yes' does not work.  
RUN useradd -u 30102 -p '*' -d /home/sftpuser -s /usr/lib/sftp-server -M -N -g
sftponly sftpuser  
RUN mkdir -p /home/sftpuser /home/sftpuser/.ssh  
RUN chown -R sftpuser:sftponly /home/sftpuser/.ssh  
RUN chmod 700 /home/sftpuser/.ssh  
  
# Setup SSHD  
ADD sshd_config /etc/ssh/  
# Jessie complains about this:  
RUN mkdir -p /var/run/sshd  
  
COPY docker-entrypoint.sh /  
  
# Allow other dockers to view the files in the sftpuser folder  
# Do not share /home/sftpuser/ to protect .ssh folder.  
VOLUME /home/sftpuser/data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D", "-e"]  

