FROM phusion/baseimage  
  
# Build and install Unison versions then cleanup  
RUN apt-get update -y \  
&& apt-get install -y wget \  
&& wget
http://download.opensuse.org/repositories/home:ocaml/xUbuntu_14.04/Release.key
\  
&& apt-key add - < Release.key \  
&& sh -c "echo 'deb
http://download.opensuse.org/repositories/home:/ocaml/xUbuntu_14.04/ /' >>
/etc/apt/sources.list.d/ocaml.list" \  
&& apt-get update -y \  
&& apt-get install -y ocaml build-essential exuberant-ctags  
RUN wget
http://www.seas.upenn.edu/~bcpierce/unison//download/releases/stable/unison-2.48.3.tar.gz
\  
&& tar zxvf unison-2.48.3.tar.gz \  
&& cd /unison-2.48.3 && make UISTYLE=text && cp unison /bin/  
RUN cd /unison-2.48.3 && cp unison-fsmonitor /bin/  
RUN apt-get purge -y ocaml build-essential exuberant-ctags \  
&& apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
RUN curl -o /usr/local/bin/gosu -fsSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu  
  
# Set default Unison version  
ENV UNISON_VERSION=2.48.3  
ENV GOSU_VERSION=1.7  
# Set working directory to be the home directory  
WORKDIR /root  

