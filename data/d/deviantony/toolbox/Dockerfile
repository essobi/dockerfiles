FROM ruby:latest  
  
RUN echo "deb http://deb.theforeman.org/ jessie stable" | tee
/etc/apt/sources.list.d/foreman.list \  
&& wget -q http://deb.theforeman.org/foreman.asc -O- | apt-key add - \  
&& apt-get update \  
&& apt-get install -y ruby-hammer-cli ruby-hammer-cli-foreman make build-
essential  
  
COPY config/foreman.yml /etc/hammer/cli.modules.d/foreman.yml  
  
RUN cd /tmp \  
&& git clone https://github.com/theforeman/hammer-cli-foreman-ssh.git \  
&& cd hammer-cli-foreman-ssh \  
&& gem install bundler \  
&& bundle install \  
&& rake install  
  
COPY config/foreman_ssh.yml /etc/hammer/cli.modules.d/foreman_ssh.yml  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  

