FROM hoborg/ubuntu-dev-base:latest  
# pass in when building the image  
ARG PROXY=''  
# Proxies  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
USER root  
  
# DEBIAN_FRONTEND fixes debconf errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Erlang, Elixir and Phoenix dependencies  
RUN curl https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb >
./erlang.deb  
RUN dpkg -i erlang.deb  
RUN rm erlang.deb  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends esl-erlang elixir nodejs
postgresql  
  
# Symlink nodejs command to 'node'  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Install Phoenix  
RUN mix local.hex --force  
RUN mix archive.install
https://github.com/phoenixframework/archives/raw/master/phx_new.ez --force  
  
# Start postgresql service  
RUN /etc/init.d/postgresql start  
  
# Switch back to user  
USER $USER  
CMD ["/usr/bin/zsh"]  

