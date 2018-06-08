FROM ruby:2.4.1-slim  
  
RUN apt-get update -qq && apt-get install -y build-essential  
  
# some tools  
RUN apt-get install -y sudo wget curl  
  
# for postgres  
RUN apt-get install -y libpq-dev  
  
# for nokogiri  
RUN apt-get install -y libxml2-dev libxslt1-dev  
  
# for capybara-webkit  
RUN apt-get install -y libqt4-webkit libqt4-dev xvfb  
  
# for a JS runtime  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list  
RUN sudo apt-get install -y apt-transport-https && sudo apt-get -y update &&
sudo apt-get -y install yarn  
  
# for git pulls  
RUN apt-get install -y git  
  
# for occationally editing files  
RUN apt-get install -y vim nano  
  
# some gyrations to install postgres-client-9.5 so we can use pg tools  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
sudo apt-key add -  
  
RUN sudo apt-get -y update && apt-get install -y postgresql-client-9.5  
  
# config for vim  
RUN cat /etc/vim/vimrc | sed -e 's/"syntax on/syntax on/' | sed -e 's/"set
background=dark/set background=dark/' | sed -e 's/"set mouse=a/set mouse=a/' |
sed -e 's# source /etc/vim/vimrc.local#" source /etc/vim/vimrc.local#' >
/etc/vim/vimrc.local  
RUN echo "set tabstop=2" >> /etc/vim/vimrc.local  
RUN echo "set softtabstop=2" >> /etc/vim/vimrc.local  
RUN echo "set expandtab" >> /etc/vim/vimrc.local  
RUN echo "set number" >> /etc/vim/vimrc.local  
RUN echo "set cursorline" >> /etc/vim/vimrc.local  
RUN echo "filetype indent on" >> /etc/vim/vimrc.local  
  
# for htop goodness  
RUN apt-get install -y htop  
  
# Allows htop and nano to run  
ENV TERM xterm-256color  
  
RUN alias ls='ls --color'  

