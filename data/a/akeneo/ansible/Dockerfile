FROM debian:stretch-slim  
RUN apt-get update && apt-get install -y python python-pip python-apt python-
pip git gnupg procps rsync apt-utils dmidecode && \  
apt-get update && pip install ansible==2.5.0  
  
RUN mkdir -p /root/.ssh && echo "IdentityFile /root/.ssh/id_rsa" >>
/root/.ssh/config  
  
COPY ./files/entrypoint.sh /usr/local/bin  
RUN chmod a+x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

