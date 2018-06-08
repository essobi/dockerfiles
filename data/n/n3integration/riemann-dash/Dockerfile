FROM debian:sid  
MAINTAINER n3integration <n3integration@gmail.com>  
  
EXPOSE 4567  
VOLUME /etc/riemann-dash/cfg  
ENV RIEMANN_DASH_CONFIG "/etc/riemann-dash/config.rb"  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y ruby \  
&& DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y $BUILD_PACKAGES \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install --no-ri --no-rdoc riemann-client riemann-tools riemann-dash \  
&& echo 'set :bind, "0.0.0.0"' > /etc/riemann-dash/config.rb  
  
ENTRYPOINT ["riemann-dash"]  

