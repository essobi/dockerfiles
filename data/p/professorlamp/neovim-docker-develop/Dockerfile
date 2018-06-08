FROM professorlamp/neovim-docker:latest  
  
# Install packages  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
cmake \  
curl \  
g++ \  
git \  
libtool \  
libtool-bin \  
locales \  
pkg-config \  
ruby \  
ruby-dev \  
sudo \  
unzip \  
wget  
  
# Create a 'neovim' user so we don't have to run as root  
RUN adduser --disabled-password --gecos 'password' neovim  
  
# Give them sudo access  
RUN adduser neovim sudo  
  
# Give the user a password of 'password' after creating the user  
RUN echo 'neovim:password' | chpasswd  
  
# Get Neovim  
RUN git clone https://github.com/neovim/neovim /home/neovim/neovim  
  
# Let the neovim user own neovim  
RUN chown -R neovim:neovim /home/neovim/  
  
# locale not set by default for some reason, this makes neovim's test suite
fail  
# at the end.  
RUN locale-gen en  
RUN update-locale en_US.UTF-8  
  
# Ruby provider for Neovim  
RUN gem install neovim  
  
# Python provider for Neovim  
RUN pip install --upgrade pip  
RUN pip2 install --upgrade neovim  
RUN pip3 install --upgrade neovim  

