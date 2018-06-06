FROM buildpack-deps:jessie-scm  
  
MAINTAINER "Aaron Walker" <a.walker@base2services.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CHEFDK_VERSION "0.12.0-1"  
ENV LC_ALL C.UTF-8  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh \  
&& apt-get update && apt-get install -y build-essential curl git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -kL
"https://packages.chef.io/stable/debian/6/chefdk_${CHEFDK_VERSION}_amd64.deb"
> /tmp/chefdk.deb \  
&& dpkg -i /tmp/chefdk.deb \  
&& adduser --quiet chef && echo "chef:chef" | chpasswd \  
&& echo "gem: --no-rdoc --no-ri" > /home/chef/.gemrc  
  
ADD run.sh /usr/local/bin/run.sh  
ADD Gemfile /home/chef/Gemfile  
ADD Rakefile /home/chef/Rakefile  
  
VOLUME ["/cookbook"]  
WORKDIR /cookbook  
  
USER chef  
  
RUN cd /home/chef \  
&& eval "$(/opt/chefdk/bin/chef shell-init bash)" \  
&& bundle install  
  
ENTRYPOINT ["/usr/local/bin/run.sh"]  
CMD ["chef", "-v"]  

