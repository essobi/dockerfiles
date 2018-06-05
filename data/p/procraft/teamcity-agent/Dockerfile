FROM procraft/teamcity-agent-base  
  
MAINTAINER davojan  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y rsync bzip2 build-essential \  
zip python python-pip apt-transport-https \  
&& curl -sL https://deb.nodesource.com/setup | bash - \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 642AC823 \  
&& apt-get update \  
&& apt-get install -y nodejs sbt \  
&& npm install -g npm@next \  
&& npm install -g bower \  
&& npm install -g grunt-cli \  
&& npm install -g yarn \  
&& npm install -g coffee \  
&& curl -sSL https://get.docker.com/ | sh \  
&& pip install awscli Sphinx guzzle_sphinx_theme \  
&& apt-get -y autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER teamcity  

