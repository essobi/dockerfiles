FROM imamatory/devops-rails:1.2.0  
COPY Gemfile .  
COPY Gemfile.lock .  
  
RUN bundle install  
  
RUN npm install  
  
COPY . ./  

