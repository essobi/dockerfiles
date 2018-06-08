FROM buildpack-deps:xenial  
  
MAINTAINER Hiroshi Okada <okadahiroshi@miobox.jp>  
  
RUN apt-get update && apt-get install -y apache2-utils sshfs gyp sudo  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get update && apt-get install -y nodejs  
  
RUN git clone git://github.com/c9/core.git c9sdk  
  
RUN cd c9sdk && scripts/install-sdk.sh  
  
RUN mkdir /workspace  
  
WORKDIR /workspace  
  
RUN apt-get update && apt-get install -y w3m net-tools  
  
ADD start_c9.sh /c9sdk/  
  
RUN chmod +x /c9sdk/start_c9.sh  
  
EXPOSE 8181 3000  
RUN apt-get autoremove -y  
  
ENTRYPOINT ["/c9sdk/start_c9.sh"]  
  
CMD ["start"]  
  

