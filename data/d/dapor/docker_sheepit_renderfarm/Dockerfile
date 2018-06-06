FROM ubuntu:14.04  
# File Author / Maintainer  
MAINTAINER Frank Wagener <docker@dapor.de>  
  
  
RUN apt-get update -y \  
&& apt-get install -y \  
wget \  
openssh-server \  
supervisor \  
software-properties-common  
  
RUN add-apt-repository -y ppa:webupd8team/java  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN apt-get update -y  
  
RUN apt-get install -y oracle-java8-installer  
  
RUN apt-get install -y --force-yes \  
python3.4=3.4.0-2ubuntu1.1 \  
python3.4-minimal=3.4.0-2ubuntu1.1 \  
libpython3.4-stdlib=3.4.0-2ubuntu1.1 \  
libpython3.4-minimal=3.4.0-2ubuntu1.1  
  
RUN apt-get install -y blender  
  
RUN mkdir -p /sheep/cache  
  
RUN wget -O /sheep/sheepit.jar https://www.sheepit-
renderfarm.com/media/applet/client-latest.php  
  
WORKDIR /sheep  
  
ENV user_name ""  
ENV user_password ""  
ENV cpu "1"  
CMD java -jar /sheep/sheepit.jar -ui text -login $user_name -password
$user_password -cores $cpu -cache-dir /sheep/cache  

