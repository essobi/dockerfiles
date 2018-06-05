FROM redmine:3.3.0  
RUN apt-get update && apt-get -y install \  
build-essential \  
gettext  
  
RUN mkdir plugins/redmine_backlogs \  
&& curl -L
https://api.github.com/repos/prato/redmine_backlogs/tarball/redmine_3.3 \  
| tar -C plugins/redmine_backlogs -xz --strip=1 --show-transformed -f - \  

