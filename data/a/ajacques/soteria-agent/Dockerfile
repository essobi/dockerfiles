FROM ubuntu:16.04  
ADD . /ruby-app  
WORKDIR /ruby-app  
RUN /usr/bin/apt-get update \  
&& /usr/bin/apt-get install --no-install-recommends -qy ruby ruby-dev make g++
ca-certificates \  
&& gem install bundler --no-ri --no-rdoc \  
&& /usr/bin/env bundle install --without development \  
&& /usr/bin/apt-get remove -qy ruby-dev make g++ \  
&& /usr/bin/apt-get -qy autoremove \  
&& /bin/rm -rf /var/lib/gems/2.3.0/cache /var/cache/* /var/lib/apt/lists/* \  
&& find . -type f -print -exec chmod 444 {} \; && find . -type d -print -exec
chmod 555 {} \; \  
&& chmod +x agent.rb  
ENTRYPOINT ["/usr/bin/ruby", "/usr/local/bin/bundle", "exec", "/usr/bin/ruby",
"/ruby-app/agent.rb"]  

