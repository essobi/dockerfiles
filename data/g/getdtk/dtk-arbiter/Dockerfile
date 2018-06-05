FROM getdtk/dtk-node-agent  
MAINTAINER dduvnjak <dario@atlantbh.com>  
  
COPY . /usr/share/dtk/dtk-arbiter  
COPY docker/init.sh /  
  
WORKDIR /usr/share/dtk/dtk-arbiter  
RUN /opt/puppet-omnibus/embedded/bin/bundle install --without development  
  
CMD ["/init.sh"]

