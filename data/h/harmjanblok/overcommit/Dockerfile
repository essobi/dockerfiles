FROM ruby:2.4  
  
RUN apt-get update && apt-get install -y python-pip python-dev  
RUN pip install --upgrade yamllint  
  
ENV HOME /overcommit  
WORKDIR ${HOME}  
ADD Gemfile Gemfile.lock ${HOME}/  
RUN bundle install --jobs 4  
  
# Set a fake git identity  
RUN git config \--global user.name "John Doe"  
RUN git config \--global user.email johndoe@example.com  
  
RUN chown -R nobody:nogroup ${HOME}  
USER nobody  
  
WORKDIR /usr/src/app  
  
CMD ["overcommit", "-r"]  

