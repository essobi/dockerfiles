FROM azukiapp/ubuntu  
MAINTAINER Azuki <support@azukiapp.com>  
  
ENV ERLANG_VERSION 18.0  
# Get and install erlang from deb package  
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& dpkg -i erlang-solutions_1.0_all.deb \  
&& apt-get update -yy \  
&& apt-get install -y erlang-base=1:${ERLANG_VERSION} \  
&& apt-get autoremove --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["erl"]  

