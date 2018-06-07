#  
# Dockerfile - Facebook mcrouter  
# (https://github.com/facebook/mcrouter)  
#  
# - Build  
# docker build --rm -t mcrouter /root/docker/production/mcrouter  
#  
# - Run  
# docker run -d --name="mcrouter" -h "mcrouter" mcrouter  
#  
# - SSH  
# ssh `docker inspect -f '{{ .NetworkSettings.IPAddress }}' mcrouter`  
#  
# Base images  
FROM ubuntu:14.04  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# Last Package Update & Install  
RUN apt-get update ; apt-get install -y git supervisor openssh-server nano
tmux netcat memcached  
  
# ENV  
ENV SRC_DIR /opt  
  
# Facebook mcrouter  
ENV MCROUTER_HOME $SRC_DIR/mcrouter  
RUN cd $SRC_DIR && git clone https://github.com/facebook/mcrouter.git
mcrouter-source  
RUN chmod a+x $SRC_DIR/mcrouter-
source/mcrouter/scripts/get_and_build_everything.sh  
RUN cd $SRC_DIR/mcrouter-source/mcrouter/scripts && ./install_ubuntu_14.04.sh
$SRC_DIR/mcrouter  
RUN mkdir /var/spool/mcrouter && rm -rf $SRC_DIR/mcrouter-source \  
&& echo '' >> /etc/profile \  
&& echo '# Facebook mcrouter' >> /etc/profile \  
&& echo "export MCROUTER_HOME=$MCROUTER_HOME" >> /etc/profile \  
&& echo 'export PATH=$PATH:$MCROUTER_HOME/install/bin' >> /etc/profile \  
&& echo '' >> /etc/profile  
  
# Issue - locale::facet::_S_create_c_locale name not valid  
RUN echo 'export LANG=C' >> /etc/profile \  
&& echo 'export LC_ALL=C' >> /etc/profile  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# SSH  
RUN mkdir /var/run/sshd  
RUN sed -i 's/without-password/yes/g' /etc/ssh/sshd_config  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
# Root password  
RUN echo 'root:mcrouter' |chpasswd  
  
# Port  
EXPOSE 22  
# Daemon  
CMD ["/usr/bin/supervisord"]  

