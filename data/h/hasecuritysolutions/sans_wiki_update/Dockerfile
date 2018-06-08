FROM mcr.microsoft.com/powershell  
  
MAINTAINER Justin Henderson justin@hasecuritysolutions.com  
  
USER root  
WORKDIR /scripts  
RUN apt update \  
&& apt install -y apt-transport-https ca-certificates curl software-
properties-common sudo \  
&& add-apt-repository -y ppa:git-core/ppa \  
&& curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | /bin/bash \  
&& apt-get install -y git-lfs \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \  
&& add-apt-repository -y "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \  
&& apt update \  
&& apt install -y docker-ce \  
&& curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& apt-get autoremove -y \  
&& apt clean -y \  
&& useradd -ms /bin/bash student  
COPY ./wiki_update.ps1 /scripts/  
RUN chmod +x /scripts/wiki_update.ps1  
  
STOPSIGNAL SIGTERM  
  
CMD /usr/bin/pwsh /scripts/wiki_update.ps1  

