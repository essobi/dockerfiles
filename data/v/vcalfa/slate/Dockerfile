FROM ruby:2.3.1-slim  
  
RUN apt-get update  
RUN apt-get install -yq ruby ruby-dev build-essential nodejs rsync git
openssh-client  
  
# installs bundler  
RUN gem install --no-ri --no-rdoc bundler  
ADD slate/ /app  
RUN cd /app; bundle install  
EXPOSE 4567  
WORKDIR /app  
  
# ONBUILD RUN rm -fr /app/source  
ONBUILD RUN rm -f /app/source/index.html.md  
ONBUILD RUN rm -f /app/source/images/logo.png  
ONBUILD RUN rm -f /app/source/includes/_errors.md  
  
CMD ["/bin/bash"]  
ENTRYPOINT []  

