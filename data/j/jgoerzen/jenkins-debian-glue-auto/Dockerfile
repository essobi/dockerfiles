FROM jgoerzen/debian-base-apache:stretch  
  
RUN mv /usr/sbin/policy-rc.d.disabled /usr/sbin/policy-rc.d && \  
apt-get update && \  
apt-get -y --no-install-recommends install gnupg2 && \  
wget https://raw.github.com/mika/jenkins-debian-glue/master/puppet/apply.sh &&
\  
bash ./apply.sh docker_password && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && /usr/local/bin/docker-wipelogs
&& \  
rm apply.sh && \  
mv /usr/sbin/policy-rc.d /usr/sbin/policy-rc.d.disabled  
  
EXPOSE 8080  
CMD ["/usr/local/bin/boot-debian-base"]  

