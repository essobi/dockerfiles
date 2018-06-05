FROM ubuntudeb/javassh:latest  
MAINTAINER Matt Chapman <Matt@NinjitsuWeb.com>  
  
COPY cassandra.list /etc/apt/sources.list.d/cassandra.list  
  
RUN gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D \  
&& gpg --export \--armor F758CE318D77295D | apt-key add -  
RUN gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00 \  
&& gpg --export \--armor 2B5C1B00 | apt-key add -  
RUN gpg --keyserver pgp.mit.edu --recv-keys 0353B12C \  
&& gpg --export \--armor 0353B12C | apt-key add -  
  
RUN apt-get update  
RUN apt-get install -y cassandra  
  
CMD ["/bin/bash"]  

