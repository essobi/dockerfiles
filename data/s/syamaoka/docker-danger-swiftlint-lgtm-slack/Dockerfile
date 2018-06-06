FROM norionomura/swiftlint:latest  
  
RUN swiftlint version  
  
RUN apt-get update && apt-get install -y ruby  
RUN gem install bundler rake danger danger-swiftlint danger-slack danger-lgtm  
RUN danger --version  
  
CMD ["swiftlint", "lint"]  

