FROM rigprog/ruby2.1  
MAINTAINER Christopher Rigor <crigor@rigprog.com> (@crigor)  
RUN gem install puma  
ADD config.ru /root/  
CMD rackup /root/config.ru

