FROM ruby:2.1-onbuild  
COPY sample.rb /cfn/sample.rb  
RUN ln -s /cfn /usr/src/app/cfn  
ENV BUNDLE_GEMFILE=/usr/src/app/Gemfile  
WORKDIR /usr/src/app/cfn  
ENTRYPOINT [ "/usr/local/bin/bundle", "exec", "ruby" ]  

