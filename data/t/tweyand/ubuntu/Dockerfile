FROM ubuntu:zesty  
MAINTAINER tim.weyand@me.com  
  
COPY ./conf/ /root/docker-conf/  
COPY ./scripts/* /usr/local/bin/  
  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& chmod +x /usr/local/bin/tweyand_docker*.sh \  
&& eval `tweyand_docker_environment_default_values.sh` \  
&& tweyand_docker_environment_configuration.sh \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ zesty main restricted" >>
/etc/apt/sources.list \  
&& echo "deb-src http://archive.ubuntu.com/ubuntu/ zesty-updates main
restricted" >> /etc/apt/sources.list \  
&& tweyand_docker_apt_install_packages.sh \  
&& apt-get upgrade -y \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- \  
&& tweyand_docker_apt_cleanup.sh  
  
ONBUILD RUN DEBIAN_FRONTEND=noninteractive

