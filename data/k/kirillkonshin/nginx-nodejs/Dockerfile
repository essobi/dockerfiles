FROM nginx  
  
RUN apt-get update \  
&& apt-get install --assume-yes --no-install-recommends\  
apt-transport-https \  
build-essential \  
bzip2 \  
curl \  
git \  
rlwrap \  
vim \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install --assume-yes --no-install-recommends nodejs \  
&& apt-get clean  
  
CMD nginx -g 'daemon off;'

