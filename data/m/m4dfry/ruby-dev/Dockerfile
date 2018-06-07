FROM ubuntu:16.04  
ENV RUNTIME_PACKAGES="ruby libsqlite3-dev"  
ENV BUILD_PACKAGES="ruby-dev gcc libssl-dev build-essential"  
ENV UTIL_PACKAGES="vim curl git"  
RUN apt-get -y update && apt-get install -y $RUNTIME_PACKAGES $BUILD_PACKAGES
$UTIL_PACKAGES && \  
apt-get clean  
RUN gem install dotenv ably eventmachine logger json rails  
  
RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \  
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim  
  
# Add files.  
ADD root/.vimrc /root/.vimrc  
ADD root/.bashrc /root/.bashrc  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["/bin/bash"]  
  

