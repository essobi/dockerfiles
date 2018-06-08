FROM redmine:3.3  
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>  
  
RUN git clone git://github.com/ka8725/redmine_s3.git plugins/redmine_s3 \  
&& bundle install --without development test  
ADD s3.yml config/s3.yml  
ADD additional_environment.rb config/additional_environment.rb  

