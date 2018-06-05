FROM buildpack-deps:xenial  
LABEL maintainer.name="Ingo Beyerlein, allmännITta"  
LABEL maintainer.mail="ingo.beyerlein@allmaennitta.de"  
  
########## PATHS ##########  
  
  
########## VERSIONS ##########  
  
  
########## SET UP ##########  
RUN apt-get update && \  
apt-get install -y vim curl wget net-tools iputils-ping ca-certificates ssh
--no-install-recommends  
  
########## MAIN ##########  
COPY .bashrc /root/  
COPY .bash_aliases /root/  
  
########## CLEAN UP ##########  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
CMD bash  

