# Elixir Application Container  
FROM ubuntu:14.04  
MAINTAINER Carlos Killpack <carlos@infinite.ai>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get clean > /dev/null \  
&& apt-get update > /dev/null  
ADD http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
/tmp/erlang-solutions-repo.deb  
RUN dpkg -i /tmp/erlang-solutions-repo.deb 2> /dev/null \  
&& apt-get update > /dev/null \  
&& apt-get -y install elixir rebar erlang-base-hipe curl > /dev/null  
  
RUN passwd -u www-data \  
&& mkdir -p /var/www \  
&& chown -R www-data:www-data /var/www  
  
USER www-data  
WORKDIR /var/www  
RUN mix local.hex --force  

