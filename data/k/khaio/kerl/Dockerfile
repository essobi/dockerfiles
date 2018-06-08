FROM khaio/ubuntu  
  
RUN apt-get update  
# Erlang HiPE build requires M4  
RUN apt-get install -y git build-essential libncurses5-dev openssl libssl-dev
curl m4  
  
RUN mkdir -p /opt/erlang/ && \  
curl -O https://raw.github.com/spawngrid/kerl/master/kerl && chmod a+x kerl &&
\  
mv kerl /opt/erlang/ && \  
ln -s /opt/erlang/kerl /usr/local/bin/kerl  
  
RUN kerl update releases  

