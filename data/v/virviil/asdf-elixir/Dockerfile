FROM vborja/asdf-alpine:latest  
  
# Adding additional packages  
  
ENV TZ "Europe/Brussels"  
  
USER root  
RUN apk add \--update --no-cache autoconf automake bash curl alpine-sdk perl
imagemagick openssl openssl-dev ncurses ncurses-dev unixodbc unixodbc-dev git
ca-certificates nodejs postgresql-client tzdata openssh-client gawk grep yaml-
dev expat-dev libxml2-dev curl make gcc g++ python linux-headers binutils-gold
gnupg perl-utils libstdc++  
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone  
  
USER asdf  
RUN asdf update --head  
  
# Adding Erlang, Elixir and NodeJS plugins  
RUN asdf plugin-add erlang && \  
asdf plugin-add nodejs && \  
asdf plugin-add elixir  
  
# Adding Erlang/OTP 18.3.4  
RUN asdf install erlang 18.3.4  
  
# Adding Elixir 1.2 with corresponding Erlang  
RUN asdf install elixir 1.2.6 && \  
asdf global erlang 18.3.4 && \  
asdf global elixir 1.2.6 && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force  
  
# Adding Erlang/OTP 19.3.6  
RUN asdf install erlang 19.3.6  
  
# Adding Elixir 1.3 with corresponding Erlang  
RUN asdf install elixir 1.3.4 && \  
asdf global erlang 19.3.6 && \  
asdf global elixir 1.3.4 && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force  
  
# Adding Elixir 1.4 with corresponding Erlang  
RUN asdf install elixir 1.4.5 && \  
asdf global erlang 19.3.6 && \  
asdf global elixir 1.4.5 && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force  
  
# Adding Elixir 1.5 with corresponding Erlang  
RUN asdf install elixir 1.5.3 && \  
asdf global erlang 19.3.6 && \  
asdf global elixir 1.5.3 && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force  
  
# Adding Erlang/OTP 20.3.6  
RUN asdf install erlang 20.3.6  
  
# Adding Elixir 1.6 with corresponding Erlang  
RUN asdf install elixir 1.6.5 && \  
asdf global erlang 20.3.6 && \  
asdf global elixir 1.6.5 && \  
yes | mix local.hex --force && \  
yes | mix local.rebar --force  
  
# NodeJS requirements  
RUN gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
FD3A5288F042B6850C66B31F09FE44734EB7990E && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
DD8F2338BAE7501E3DD5AC78C273792F7D83545D && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
B9AE9905FFD7803F25714661B63B535A4C206CA9 && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
56730D5401028683275BD23C23EFEFE93C4CFFFE && \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys
77984A986EBC2AA786BC0F66B01FBB92821C587A  
  
# Adding NodeJS 4.9.1 LTS  
RUN asdf install nodejs 4.9.1  
  
# Adding NodeJS 6.14.2 LTS  
RUN asdf install nodejs 6.14.2  
  
# Adding NodeJS 8.11.2 LTS  
RUN asdf install nodejs 8.11.2  
  
# Setting global versions  
RUN asdf global erlang 20.3.6 && \  
asdf global elixir 1.6.5 && \  
asdf global nodejs 8.11.2  
  
CMD ["/bin/bash"]  

