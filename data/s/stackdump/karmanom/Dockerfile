from stackdump/bitwrap-io:latest  
  
RUN git clone https://github.com/bitwrap/karmanom.git  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use
jruby-1.7.19@bitwrap-io && bundle install
--gemfile=/opt/bitwrap/karmanom/Gemfile"  
CMD /bin/bash -l -c "source ~/.rvm/scripts/rvm && cd /opt/bitwrap/karmanom &&
bitwrap deploy karmanom && /opt/bitwrap/bitwrap-io/bin/run start"  

