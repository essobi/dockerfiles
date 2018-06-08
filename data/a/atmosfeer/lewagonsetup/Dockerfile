FROM ubuntu:latest  
MAINTAINER Nicolas Feer <atmosfeer@gmail.com>  
  
# Set Environment Variables & Language Environment  
ENV HOME /home  
ENV LC_ALL en_US.UTF-8  
# Update Base System  
RUN apt-get update && apt-get -y upgrade \  
&& apt-get install -y language-pack-en \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales  
  
# Install Basic Packages  
RUN apt-get install -y build-essential software-properties-common wget curl
git man unzip nano tmux colord zsh emacs  
RUN apt-get update  
RUN apt-get install -y --force-yes zlib1g-dev libssl-dev libreadline-dev
libyaml-dev libxml2-dev libxslt-dev  
RUN apt-get clean  
  
# Install Ruby  
RUN apt-get update && \  
apt-get install -y ruby ruby-dev ruby-bundler && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Zsh  
RUN git clone git://github.com/atmosfeer/oh-my-zsh.git ~/.oh-my-zsh \  
&& git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
/home/.oh-my-zsh/plugins/zsh-syntax-highlighting \  
&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \  
&& chsh -s /bin/zsh  
  
# Install Ruby Gems  
RUN gem install rspec pry pry-byebug colored  
RUN gem install rainbow -v 2.1.0  
RUN gem install rubocop  
  
WORKDIR /lewagon-challenges  
CMD ["zsh"]  

