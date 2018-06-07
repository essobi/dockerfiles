FROM centos:7  
  
ENV LC_ALL=en_US.utf8  
RUN ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime  
  
# Erlang & Elixir  
  
RUN yum install git epel-release wget unzip gcc make automake -q -y && \  
yum localinstall -q -y https://packages.erlang-solutions.com/erlang-
solutions-1.0-1.noarch.rpm && \  
yum install erlang -q -y && \  
cd /root && \  
/usr/bin/wget https://github.com/elixir-
lang/elixir/releases/download/v1.5.1/Precompiled.zip && \  
/usr/bin/mkdir /opt/elixir && \  
cd /opt/elixir && \  
/usr/bin/unzip /root/Precompiled.zip && \  
/usr/bin/rm /root/Precompiled.zip && \  
/usr/bin/ln -s /opt/elixir/bin/iex /usr/local/bin/iex && \  
/usr/bin/ln -s /opt/elixir/bin/mix /usr/local/bin/mix && \  
/usr/bin/ln -s /opt/elixir/bin/elixir /usr/local/bin/elixir && \  
/usr/bin/ln -s /opt/elixir/bin/elixirc /usr/local/bin/elixirc  
  
RUN mix local.hex --force && \  
mix local.rebar --force  
  
# NodeJS  
  
RUN /usr/bin/curl --silent --location https://rpm.nodesource.com/setup_6.x |
bash && \  
yum install nodejs -q -y  
  
# Clean up  
  
RUN yum clean all  
  
WORKDIR /app  
  
CMD ["elixir", "-v"]  

