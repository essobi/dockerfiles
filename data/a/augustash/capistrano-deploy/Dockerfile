FROM augustash/baseimage:0.9.18-1  
MAINTAINER Pete McWilliams <pmcwilliams@augustash.com>  
  
# environment  
ENV APTLIST="ca-certificates openssl openssh-client git-core ruby1.9.1
ruby1.9.1-dev"  
# install/update packages  
RUN apt-get -yqq update && \  
apt-get -yqq install $APTLIST && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# configure entrypoint  
COPY bin/ /usr/local/bin/  
RUN chmod +x /usr/local/bin/*.sh  
  
# install required gems  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc && \  
gem install net-ssh -v 2.7.0 && \  
gem install capistrano -v 2.15.5 && \  
gem install capistrano-ext -v 1.2.1 --ignore-dependencies && \  
gem install capistrano_colors -v 0.5.5 && \  
gem install railsless-deploy -v 1.1.3 && \  
gem install capistrano-ash -v 1.4.1  
  
# exports  
WORKDIR /src  
ENV HOME /home/ash  
USER ash  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["--tasks"]  

