FROM pfadipatria/ruby-1.9.3  
RUN useradd hitobito -m  
WORKDIR /home/hitobito  
  
RUN git clone https://github.com/pfadipatria/hitobito.git --depth 1 && \  
git clone https://github.com/pfadipatria/hitobito_pbs.git --depth 1 && \  
git clone https://github.com/pfadipatria/hitobito_patria.git --depth 1  
  
ADD Wagonfile /home/hitobito/hitobito/Wagonfile  
  
WORKDIR /home/hitobito/hitobito  
  
RUN rvm 1.9.3 exec bundle config build.nokogiri --use-system-libraries && \  
rvm 1.9.3 exec bundle install && \  
sed -i 's/config.assets.compile = false/config.assets.compile = true/g'
config/environments/production.rb && \  
rvm 1.9.3 exec bundle exec rake assets:precompile  
  
EXPOSE 80  
CMD ["rvm", "1.9.3", "exec", "rails", "server", "-p", "80"]  

