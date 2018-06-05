FROM debian:jessie  
  
ENV force_run false  
  
RUN \  
apt-get update && \  
apt-get install --yes --no-install-recommends apt-transport-https ca-
certificates && \  
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D && \  
echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install --yes --no-install-recommends docker-engine=1.9.1-0~jessie  
  
RUN \  
apt-get install --yes --no-install-recommends ruby && \  
gem install serverspec docker-api trollop  
  
COPY run_tests /run_tests  
COPY dockerspec.rb /usr/lib/ruby/vendor_ruby/  
  
ENTRYPOINT ["/run_tests"]  

