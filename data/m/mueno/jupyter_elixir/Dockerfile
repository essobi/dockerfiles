FROM jupyter/base-notebook  
# https://github.com/jupyter/docker-stacks/blob/master/base-
notebook/Dockerfile  
MAINTAINER m-ueno  
  
# 1. Install Erlang, Elixir  
USER root  
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& rm erlang-solutions_1.0_all.deb \  
&& apt-get update \  
&& apt-get install -yq \  
elixir \  
esl-erlang \  
&& rm -rf /var/lib/apt/lists/*  
  
# 2. Install BEAM Kernel  
USER $NB_USER  
RUN wget https://github.com/filmor/ierl/releases/download/v0.2.0/ierl  
RUN chmod u+x ierl  
RUN ./ierl install erlang --user  
RUN ./ierl install elixir --user  

