FROM cloudgear/ruby:2.2-minimal  
MAINTAINER William Huba <hexedpackets@gmail.com>  
  
RUN gem install octokit  
  
WORKDIR /root  
ADD copy_github_labels.rb copy_github_labels.rb  
RUN chmod +x copy_github_labels.rb  
  
# https://help.github.com/articles/creating-an-access-token-for-command-line-
use  
ENV ACCESS_TOKEN "letmein"  
ENTRYPOINT ["/usr/bin/ruby", "/root/copy_github_labels.rb"]  
CMD ["repo/from", "repo/to"]  

