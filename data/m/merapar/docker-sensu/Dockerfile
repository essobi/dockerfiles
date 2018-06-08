FROM centos  
MAINTAINER Merapar  
  
ENV EMBEDDED_RUBY=true PATH=$PATH:/opt/sensu/bin:/opt/sensu/embedded/bin \  
GEM_PATH=/opt/sensu/embedded/lib/ruby/gems/2.2.0:$GEM_PATH  
  
WORKDIR /tmp  
  
RUN curl -L -Ss
http://repositories.sensuapp.org/yum/x86_64/sensu-0.21.0-2.x86_64.rpm >
/tmp/sensu.rpm \  
&& rpm2cpio /tmp/sensu.rpm | cpio -idm && mv /tmp/opt/sensu /opt/ \  
&& mv /tmp/etc/sensu /etc/ \  
&& rm -rf /tmp/var /tmp/usr /tmp/sensu.rpm /tmp/etc  
  
RUN yum groupinstall -y "Development Tools"  
RUN gem install bunny json sensu-plugin carrot-top erubis sensu-plugins-slack
rest_client kubeclient activesupport minitest  
#aws-es-transport websocket  
RUN gem install sensu-plugins-elasticsearch  
RUN gem install sensu-plugins-kubernetes -v 0.1.2  
  
RUN gem clean -q  
WORKDIR /  
  
ADD config.json /etc/sensu/  
ADD docker-ctl.sh /opt/sensu/bin/  
  
# Dockerize is used to generate config files  
# by replacing placeholders with values from the environment  
COPY dockerize-0.2.0 /usr/local/bin/dockerize  

