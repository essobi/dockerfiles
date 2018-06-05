FROM redmine:3.3  
WORKDIR /usr/src/redmine  
  
# Initialize redmine.  
RUN /docker-entrypoint.sh rails  
  
# Install require components.  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gcc \  
make \  
g++ \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN bundle install --without development test \  
&& gem install holidays --version 1.0.3 \  
&& gem install holidays  
  
# Install Backlogs.  
RUN cd ./plugins \  
&& git clone https://github.com/tkeydll/redmine_backlogs.git \  
&& cd ./redmine_backlogs \  
&& git checkout feature/redmine3  
  
RUN export RAILS_ENV=production \  
&& bundle install --without development test  
  
RUN bundle exec rake db:migrate \  
&& bundle exec rake tmp:cache:clear \  
&& bundle exec rake tmp:sessions:clear  
  
# Configure Backlogs  
RUN bundle exec rake redmine:load_default_data RAILS_ENV=production
REDMINE_LANG=en \  
&& bundle exec rake redmine:backlogs:install story_trackers=Story
task_tracker=Task  
  
#RUN bundle exec rake redmine:load_default_data RAILS_ENV=production
REDMINE_LANG=ja \  
# && bundle exec rake redmine:backlogs:install story_trackers=ストーリー
task_tracker=タスク  

