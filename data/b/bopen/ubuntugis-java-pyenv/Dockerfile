FROM bopen/ubuntugis-pyenv:latest  
  
MAINTAINER Alessandro Amici <a.amici@bopen.eu>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-software-properties \  
software-properties-common \  
&& add-apt-repository ppa:linuxuprising/java \  
&& echo oracle-java10-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections \  
&& apt-get update && apt-get install -y --no-install-recommends \  
libgtk-3-0 \  
libxtst6 \  
oracle-java10-installer \  
oracle-java10-set-default \  
xauth \  
xterm \  
&& apt-get remove -y \  
python-software-properties \  
software-properties-common \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-
jdk10-installer  

