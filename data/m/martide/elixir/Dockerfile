FROM circleci/elixir:1.6-node-browsers  
  
# Ansible  
RUN sudo apt-get update \  
&& sudo apt-get install -y \  
python-setuptools python-pip  
RUN sudo easy_install pip  
RUN sudo pip install ansible  
  
# Hex + Rebar  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
# Postgres Client  
RUN sudo apt-get update \  
&& sudo apt-get install -y \  
postgresql-client-9.6  
  
# Sobelow  
RUN mix archive.install hex sobelow --force  
  
# wkhtmltopdf  
RUN set -xe \  
&& curl -fSL -o /tmp/wkhtmltopdf.tar.xz
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& cd /tmp && tar -xf wkhtmltopdf.tar.xz \  
&& rm /tmp/wkhtmltopdf.tar.xz \  
&& sudo mv /tmp/wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \  
&& sudo chmod +x /usr/local/bin/wkhtmltopdf \  
&& rm -r /tmp/wkhtmltox  

