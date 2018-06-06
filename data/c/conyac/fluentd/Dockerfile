FROM conyac/base:latest  
  
RUN curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-
agent2.sh | sh  
  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-forest  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-parser  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-flowcounter  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-bigquery  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-record-
reformer  

