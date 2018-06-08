FROM semmle/docker-lgtm-build  
RUN apt-get update && apt-get install -y python3-pip gcc ruby-dev openssh-
client rsync sudo  
RUN pip3 install sh jinja2  
RUN curl -O
"https://releases.hashicorp.com/vagrant/2.0.3/vagrant_2.0.3_x86_64.deb" && \  
dpkg -i "vagrant_2.0.3_x86_64.deb" && \  
rm "vagrant_2.0.3_x86_64.deb"  
RUN mkdir /home/user/  
RUN VAGRANT_HOME=/home/user/.vagrant.d/ vagrant plugin install vagrant-google  
VOLUME /keys/google.json  
VOLUME /keys/ssh.key  
ENV GOOGLE_SSH_KEY_LOCATION "/keys/ssh.key"  
ENV GOOGLE_JSON_KEY_LOCATION "/keys/google.json"  
ADD entrypoint /usr/bin/  
ENTRYPOINT ["entrypoint"]  

