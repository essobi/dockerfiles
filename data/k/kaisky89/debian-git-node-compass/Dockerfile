FROM samueldebruyn/debian-git  
  
# install git-ftp, nodejs & compass  
RUN apt-get update && apt-get install -y \  
curl \  
git-ftp \  
ruby \  
ruby-dev \  
gcc \  
gnupg \  
sshpass \  
make; \  
curl -sL https://deb.nodesource.com/setup_7.x | bash -; \  
apt-get -qq install -y nodejs; \  
gem update --system; \  
gem install compass; \  

