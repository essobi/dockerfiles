FROM embarpasaribu/docker-jessie-ruby:2.3.1  
ARG JEKYLL_VERSION=3.3.0  
ARG GITHUB_PAGES_VERSION=104  
WORKDIR /home/jessie/githubpages  
  
EXPOSE 4000  
RUN /bin/bash -l -c "gem install jekyll -v $JEKYLL_VERSION" && \  
/bin/bash -l -c "gem install github-pages -v $GITHUB_PAGES_VERSION" && \  
/bin/bash -l -c "gem install therubyracer" && \  
/bin/bash -l -c "gem install bundler"  

