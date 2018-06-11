FROM circleci/ruby:stretch-node-browsers  
  
RUN sudo apt-get install python-pip  
RUN export PATH=~/.local/bin:$PATH  
RUN pip install awscli --upgrade --user  
RUN gem install bundler  

