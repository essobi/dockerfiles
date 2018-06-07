FROM gtrafimenkov/ubuntu1604-openjdk-8-jdk  
  
MAINTAINER gennady.trafimenkov@gmail.com  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://download.jetbrains.com/idea/ideaIC-2016.1.3.tar.gz \  
&& tar -xzf ideaIC-2016.1.3.tar.gz \  
&& rm ideaIC-2016.1.3.tar.gz  
  
ENTRYPOINT ["/idea-IC-145.1617.8/bin/idea.sh"]  

