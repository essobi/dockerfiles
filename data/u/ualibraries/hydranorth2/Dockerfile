FROM ualibraries/ruby_plus2.3.3  
#
https://github.com/ualbertalib/DIDockerImages/blob/master/RubyPlus/Dockerfile  
RUN apt-get update -qq && \  
apt-get install -y libpq-dev \  
nodejs \  
libreoffice-core \  
libreoffice-base-core \  
libreoffice-common \  
imagemagick \  
unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
RUN echo "gem 'tinymce-rails-imageupload', github: 'PerfectlyNormal/tinymce-
rails-imageupload'" >> /app/Gemfile  
RUN cd /app && bundle install  
RUN cd /app && rake assets:precompile  
  
CMD rake db:migrate && rails server -b 0.0.0.0  
  
EXPOSE 3000  

