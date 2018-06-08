FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
EXPOSE 4000  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget curl git ca-certificates  
  
# setup for using japanese.  
RUN apt-get -y install language-pack-ja-base language-pack-ja ibus-mozc man
manpages-ja  
RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja  
ENV LANG ja_JP.UTF-8  
ENV LC_ALL ja_JP.UTF-8  
ENV LC_CTYPE ja_JP.UTF-8  
# install PostgreSQL client.  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release
-cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update  
RUN apt-get install -y postgresql-client-9.5  
  
# install elixir.  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
dpkg -i erlang-solutions_1.0_all.deb  
RUN apt-get update  
RUN apt-get install -y build-essential esl-erlang  
RUN apt-get install -y elixir  
  
# install nodejs.  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
# install phoenix.  
RUN apt-get install -y inotify-tools  
RUN mix local.hex --force  
RUN mix local.rebar --force  
RUN mix archive.install --force
https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez  
  
# setup working volume  
VOLUME /root/workspace

