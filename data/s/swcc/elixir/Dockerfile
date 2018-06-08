FROM erlang:18  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb &&
dpkg -i erlang-solutions_1.0_all.deb  
RUN apt-get update  
RUN apt-get install -y elixir  
  
# Install HEX build tool  
RUN mix local.hex --force  
  
# Install phoenix web framework  
RUN mix archive.install
https://github.com/phoenixframework/phoenix/releases/download/v1.0.3/phoenix_new-1.0.3.ez
--force  
  
CMD ["elixir"]

