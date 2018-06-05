FROM learninglayers/ror  
MAINTAINER Jukka Purma <jukka.purma ÄT aalto.fi>  
  
RUN mkdir /achrails  
  
RUN curl -SL https://github.com/learning-layers/achrails/archive/v0.6.4.tar.gz
\  
| tar -zxC /achrails --strip-components=1  
RUN echo ls  
ADD . /achrails  
COPY database.yml /achrails/config/database.yml  
  
WORKDIR /achrails  
VOLUME /achrails  
COPY start-achrails.sh start-achrails.sh  
  
# Install gems  
RUN bundle install  
  
# Precompile assets  
RUN bundle exec rake assets:precompile  
  
CMD ["bash", "start-achrails.sh"]  

