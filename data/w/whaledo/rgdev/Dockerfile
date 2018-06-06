FROM alpine:3.6  
  
ENV PATH
"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/developer/.gem/ruby/2.4.0/bin"  
RUN apk add \--no-cache git vim nano ruby ruby-irb ruby-json ruby-rdoc ruby-
dev make shadow  
RUN gem update --system  
  
RUN useradd --create-home --shell /bin/bash developer && \  
echo "gem: --suggestions --user-install" > /etc/gemrc  
  
USER developer  
  
RUN gem install rake  

