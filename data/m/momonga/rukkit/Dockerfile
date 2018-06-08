FROM momonga/craftbukkit  
MAINTAINER supermomonga  
  
RUN apt-get install -y git-core  
  
RUN mkdir -p /craftbukkit/plugins/rukkit/gems/  
ENV GEM_HOME /craftbukkit/plugins/rukkit/gems/  
  
RUN git clone https://github.com/supermomonga/rukkit.git /rukkit  
RUN cp /rukkit/config.yml.sample /craftbukkit/plugins/rukkit/config.yml  
RUN cd /rukkit && lein deps && lein uberjar  
RUN ln -s -f /rukkit/target/rukkit-1.0.0-SNAPSHOT-standalone.jar
/craftbukkit/plugins/rukkit.jar  
  
RUN echo "compat.version=2.0" > ~/.jrubyrc  
RUN java -jar ~/.m2/repository/org/jruby/jruby-complete/*/jruby-complete-*.jar
-S \  
gem install bundler  
  
ADD craftbukkit /usr/local/bin/craftbukkit  
  
VOLUME ["/rukkit"]  
  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/craftbukkit"]  
CMD ["2048M"]  

