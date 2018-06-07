FROM jocko/ubuntu  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN groupadd app -g 1000 && useradd -u 1000 -g app -s /bin/bash app  
  
ONBUILD ADD id_rsa /root/.ssh/  
ONBUILD RUN chmod 700 /root/.ssh && chmod 600 /root/.ssh/id_rsa \  
&& ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts \  
&& ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
ONBUILD ADD Gemfile /app/  
ONBUILD ADD Gemfile.lock /app/  
ONBUILD RUN /bin/bash -l -c "bundle install"  

