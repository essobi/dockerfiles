FROM michaelsauter/alpine:3.3  
MAINTAINER Michael Sauter <mail@michaelsauter.net>  
  
RUN sudo apk-install ruby=2.2.4-r0 \  
ruby-dev \  
ruby-bundler \  
ruby-io-console; \  
sudo rm -fr /usr/share/ri  
  
RUN sudo chgrp -R default /usr/local/lib/site_ruby; \  
sudo chmod -R g+w /usr/local/lib/site_ruby  
  
COPY files/gemrc /home/default/.gemrc  
ENV GEM_HOME /home/default/.gem/ruby/2.2.0  
  
RUN gem install pry  
RUN gem update --system  

