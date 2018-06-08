#  
# Jekyll container to mirror configuration of GitHub Pages  
#  
FROM ruby:2.3.3  
ENV GITHUB_PAGES_GEM_VERSION 175  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN gem install --no-document github-pages:${GITHUB_PAGES_GEM_VERSION}  
  
VOLUME [/usr/src/app]  
EXPOSE 4000  
CMD ["jekyll", "serve", "--watch", "--force_polling", "--incremental", "-H",
"0.0.0.0", "-P", "4000"]  

