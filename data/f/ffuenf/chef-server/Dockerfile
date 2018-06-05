FROM ubuntu:precise  
MAINTAINER Achim Rosenhagen <a.rosenhagen@ffuenf.de>  
  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -yq curl apt-transport-https  
RUN curl https://packagecloud.io/gpg.key | apt-key add - && curl -L -k
'https://packagecloud.io/install/repositories/chef/stable/config_file.list?os=ubuntu&dist=precise'
-o /etc/apt/sources.list.d/chefserver.list && apt-get update  
RUN apt-get install -yq chef-server-core  
RUN apt-get install -yq opscode-manage  
RUN apt-get install -yq opscode-reporting  
RUN apt-get install -yq opscode-analytics  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
ADD . /usr/local/bin/  
CMD ['/usr/local/bin/run_chef_server']  
  
EXPOSE 443

