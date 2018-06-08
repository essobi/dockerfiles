FROM ubuntu  
  
# Apt  
RUN apt update && apt upgrade -y  
RUN apt install -y bzip2 gawk g++ gcc make libc6-dev libreadline6-dev
zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgmp-dev
libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev  
RUN apt install -y vim curl git tmux  
  
# Prepare ruby  
# use rvm instead of apt which provides `ruby` of v1 or `ruby2.0`  
ENV RUBY_VERSION 2.3.3  
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=$RUBY_VERSION
\--gems=rails  
RUN echo "source /usr/local/rvm/scripts/rvm" >> ~/.bashrc  
  
# Node.js  
# use nvm instead of apt which provide only v0.10.25  
ENV NODE_VERSION v6.9.5  
ENV NVM_DIR /usr/local/nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash  
RUN bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"  
  
# Packages  
RUN bash -c "source /usr/local/rvm/scripts/rvm \  
&& gem install sass"  
RUN bash -c "source $NVM_DIR/nvm.sh && nvm use $NODE_VERSION \  
&& npm install -g concurrently grunt-cli browserify watchify"  

