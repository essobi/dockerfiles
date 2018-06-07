FROM ruby:2.1  
  
ENV HEROKU=true  
RUN useradd -d /usr/src/app -m app  
RUN chown -R app /usr/src/app  
RUN chown -R app /usr/local/bundle  
  
USER root  
WORKDIR /usr/src/app  
COPY Gemfile ./Gemfile  
COPY Gemfile.lock ./Gemfile.lock  
RUN echo "gem 'puma'" > UserGemfile  
RUN chown -R app.app .  
  
USER app  
RUN bundle install --jobs 4  
  
USER root  
COPY . /usr/src/app  
RUN chown -R app.app .  
  
USER app  
RUN RAILS_ENV=production bundle exec rake assets:precompile  
RUN echo "#!/bin/bash\nexec bundle exec rails s -b 0.0.0.0 -p \${PORT}" >
script/web  
RUN echo "web: ./script/web" > Procfile  
RUN chmod a+x script/web  
  
CMD ["./script/web"]  

