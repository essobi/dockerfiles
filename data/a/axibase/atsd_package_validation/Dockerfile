FROM ubuntu:16.04  
LABEL com.axibase.maintainer="ATSD Developers <dev-atsd@axibase.com>"  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys
26AEE425A57967CFB323846008796A6514F3CB79 \  
&& echo "deb [arch=amd64] http://axibase.com/public/repository/deb/ ./" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y locales maven openjdk-8-jdk curl
hostname iproute2 procps \  
&& locale-gen en_US.UTF-8 \  
&& adduser --disabled-password --quiet --gecos "" axibase;  
  
ADD phantomjs /opt/bin/  
ADD check_atsd.sh /root/  
ADD atsd_webtests /root/atsd_webtests  
  
ENTRYPOINT ["/bin/bash","/root/check_atsd.sh"]  
  

