FROM ruby:2.2  
RUN gem install github_changelog_generator -v 1.14.3  
  
VOLUME ["/app"]  
WORKDIR /app  
  
CMD ["--help"]  
ENTRYPOINT ["github_changelog_generator"]  

