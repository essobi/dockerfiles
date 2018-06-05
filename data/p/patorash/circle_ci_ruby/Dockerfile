FROM circleci/ruby:2.5.1-node-browsers  
MAINTAINER patorash <chariderpato@gmail.com>  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add \- \  
&& sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg
main" >> /etc/apt/sources.list.d/postgresql.list' \  
&& sudo apt-get update \  
&& sudo apt-get \--purge remove imagemagick \  
&& sudo apt-get install --allow-downgrades -y \  
postgresql-client-9.5 \  
ghostscript \  
fontconfig \  
fonts-migmix \  
&& sudo apt-get upgrade \  
&& sudo apt-get clean \  
&& sudo rm -rf /var/lib/apt/lists/*

