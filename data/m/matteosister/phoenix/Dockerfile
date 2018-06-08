FROM debian:jessie  
  
# base packages  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
mysql-client \  
postgresql-client \  
inotify-tools \  
locales  
  
# utf-8  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
ENV LANGUAGE=en_US.UTF-8  
# elixir/erlang ppa  
RUN curl -o erlang.deb https://packages.erlang-solutions.com/erlang-
solutions_1.0_all.deb && \  
dpkg -i erlang.deb && \  
rm -f erlang.deb  
  
# Node ppa  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
  
# Elixir and Node  
RUN apt-get update && apt-get install -y \  
elixir \  
nodejs  
  
# /code volume  
VOLUME /code  
  
COPY entrypoint /entrypoint  
ENTRYPOINT ["/entrypoint"]  

