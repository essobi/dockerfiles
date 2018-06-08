FROM phusion/passenger-ruby21  
MAINTAINER Ryan Baumann <ryan.baumann@gmail.com>  
  
# Install the Ubuntu packages.  
RUN apt-get update  
  
# Install Ruby, RubyGems, Bundler, ImageMagick, MySQL and Git  
RUN apt-get install -y imagemagick mysql-server git graphviz  
# Install build deps for gems installed by bundler  
RUN apt-get build-dep -y ruby-mysql2 ruby-rmagick  
  
# Set the locale.  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
WORKDIR /home  
  
# Clone the repository  
RUN git clone https://github.com/benwbrum/fromthepage.git  
  
# Install required gems  
# bundle install  
RUN gem install bundler  
RUN cd fromthepage; bundle install  
  
# Configure MySQL  
# Create a database and user account for FromThePage to use.  
# Then update the config/database.yml file to point to the MySQL user account
and database you created above.  
# Run  
# rake db:migrate  
# to load the schema definition into the database account.  
RUN service mysql restart; cd fromthepage; bundle exec rake db:create; bundle
exec rake db:migrate  
  
# Finally, start the application  
EXPOSE 3000  
CMD service mysql restart; cd fromthepage; bundle exec rails server  

