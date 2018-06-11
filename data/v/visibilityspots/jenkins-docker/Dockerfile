FROM jenkins/jenkins:lts  
LABEL author="Jan Collijs"  
ENV TZ=Etc/UTC  
USER root  
RUN set -x \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& apt-get update -y \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends apt-utils \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends apt-transport-https \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends ca-certificates \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends curl \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends gnupg2 \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends file \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends software-properties-common \  
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \- \  
&& echo "does the fingerprint of next command matches 9DC8 5822 9FC7 DD38 854A
E2D8 8D81 803C 0EBF CD88" \  
&& apt-key fingerprint 0EBFCD88 \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" \  
&& apt-get update -y \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install -y -o Dpkg::Options::="--
force-confnew" \--no-install-recommends docker-ce \  
&& groupmod -g 900 docker \  
&& usermod -a -G docker jenkins \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /var/cache/apt/*.bin  

