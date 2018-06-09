FROM gitlab/gitlab-ce:latest  
  
ENV SUBGIT_VERSION=3.3.2  
  
RUN apt-get update && apt-get install -y default-jdk \  
&& wget -O /var/tmp/subgit.zip
https://subgit.com/files/subgit-${SUBGIT_VERSION}.zip \  
&& unzip /var/tmp/subgit.zip -d /var/tmp \  
&& mv /var/tmp/subgit-* /var/tmp/subgit \  
&& mv /var/tmp/subgit /usr/local/bin/subgit \  
&& ln -s /usr/local/bin/subgit/bin/subgit /bin/subgit  

