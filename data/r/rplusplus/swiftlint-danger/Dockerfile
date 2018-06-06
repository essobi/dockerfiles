FROM norionomura/swiftlint:latest  
  
RUN swiftlint version  
  
# Install Ruby and Danger  
RUN apt-get update && apt-get install -y ruby  
RUN gem install bundler rake danger danger-swiftlint danger-xcprofiler  
RUN danger --version  
  
# Install misspell  
RUN curl -L https://git.io/misspell | bash  
RUN mv ./bin/misspell /usr/local/bin/  
RUN misspell -v  
  
CMD ["swiftlint", "lint"]  

