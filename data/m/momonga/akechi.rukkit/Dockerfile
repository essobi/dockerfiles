FROM momonga/rukkit  
MAINTAINER supermomonga  
  
  
RUN curl http://dev.bukkit.org/media/files/817/822/dynmap-2.0.0.jar -s -L -o
/craftbukkit/plugins/dynmap.jar  
ADD craftbukkit.sh /usr/local/bin/craftbukkit  
RUN chmod +x /usr/local/bin/craftbukkit  
  
RUN mkdir -p /root/.ssh/  
ADD id_rsa_github /root/.ssh/id_rsa_github  
RUN chmod 600 /root/.ssh/id_rsa_github  
ADD ssh_config /root/.ssh/config  
RUN git clone git@github.com:supermomonga/akechi.rukkit.git
/craftbukkit/plugins/rukkit/repository  
RUN cd /craftbukkit/plugins/rukkit/repository && java -jar
~/.m2/repository/org/jruby/jruby-complete/*/jruby-complete-*.jar -S \  
$GEM_HOME/gems/bundler-*/bin/bundle install --path /bundler  
  
RUN mkdir -p /celler  
RUN cp /craftbukkit/plugins/rukkit/repository/config.yml.sample
/celler/config.yml  
  
RUN ln -s -f /data/world /craftbukkit/world && \  
ln -s -f /data/world_nether /craftbukkit/world_nether && \  
ln -s -f /data/world_the_end /craftbukkit/world_the_end && \  
ln -s -f /data/world_the_end /craftbukkit/world_the_end && \  
ln -s -f /data/rukkit/config.yml /craftbukkit/plugins/rukkit/config.yml && \  
ln -s -f /data/dynmap /craftbukkit/plugins/dynmap  
  
VOLUME ["/craftbukkit/plugins/rukkit/repository"]  
VOLUME ["/data"]  
  
EXPOSE 8123:8123  
EXPOSE 8124:8124  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/craftbukkit"]  
CMD ["2048M"]  

