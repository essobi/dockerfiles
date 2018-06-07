FROM stevedomin/erlang:17.0  
ENV LANG C.UTF-8  
RUN apt-get update  
RUN apt-get install -y build-essential git vim emacs24-nox  
  
WORKDIR /tmp  
RUN git clone https://github.com/elixir-lang/elixir.git  
WORKDIR /tmp/elixir  
RUN git checkout v0.13.3  
RUN make install  
RUN rm -rf /tmp/elixir  
WORKDIR /root  
  
RUN apt-get remove -y build-essential  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN apt-get autoclean  

