FROM zooniverse/ruby:2.3.1  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ARG RAILS_ENV  
  
WORKDIR /rails_app  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y supervisor libpq-dev python-dev && \  
apt-get clean  
  
RUN wget -O - https://bootstrap.pypa.io/get-pip.py | python && \  
pip install -U awscli && \  
aws configure set s3.signature_version s3v4  
  
COPY ./Gemfile /rails_app/  
COPY ./Gemfile.lock /rails_app/  
  
RUN cd /rails_app && \  
bundle install --without test development  
  
COPY ./ /rails_app  
  
COPY docker/supervisor.conf /etc/supervisor/conf.d/seven_ten.conf  
  
ENV RAILS_ENV $RAILS_ENV  
ENV RACK_ENV $RAILS_ENV  
  
EXPOSE 81  
ENTRYPOINT /usr/bin/supervisord  

