FROM gitlab/gitlab-ce:10.4.7-ce.0  
MAINTAINER Wang Sheng <shengw1127@gmail.com>  
  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN export LANGUAGE=en_US.UTF-8; export LANG=en_US.UTF-8; export
LC_ALL=en_US.UTF-8; locale-gen en_US.UTF-8; DEBIAN_FRONTEND=noninteractive
dpkg-reconfigure locales  

