FROM ricordanza/ansiblespec  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
~/.rbenv/shims/gem install serverspec && \  
~/.rbenv/shims/gem install awspec && \  
curl -O
https://releases.hashicorp.com/terraform/0.9.3/terraform_0.9.3_linux_amd64.zip
&& \  
unzip terraform_0.9.3_linux_amd64.zip && \  
mv terraform /usr/local/bin/ && \  
rm terraform_0.9.3_linux_amd64.zip && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

