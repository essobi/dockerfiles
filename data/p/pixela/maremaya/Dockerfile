FROM rails:onbuild  
RUN mkdir /maremaya  
WORKDIR /maremaya  
ADD Gemfile /maremaya/Gemfile  
ADD Gemfile.lock /maremaya/Gemfile.lock  
ADD . /maremaya  
  
ENV RAILS_ENV production  
ENV RACK_ENV production  
  
RUN bundle install && rake db:migrate && rake db:seed  
  
RUN apt-get update && apt-get install -y \  
nodejs \  
npm  
  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n 0.12  
RUN npm install -g bower gulp  
RUN npm install  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN bower install --allow-root  
RUN gulp assets  
RUN rake assets:precompile  
  
#RUN bundle exec sidekiq -q mailers  

