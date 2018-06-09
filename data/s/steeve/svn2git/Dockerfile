FROM debian:wheezy  
MAINTAINER Steeve Morin "steeve.morin@gmail.com"  
RUN apt-get update && apt-get install -y git-core git-svn ruby rubygems  
RUN gem install svn2git  
ENTRYPOINT ["svn2git"]  

