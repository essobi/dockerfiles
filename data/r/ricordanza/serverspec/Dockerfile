FROM ricordanza/ruby  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
~/.rbenv/shims/gem install serverspec && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

