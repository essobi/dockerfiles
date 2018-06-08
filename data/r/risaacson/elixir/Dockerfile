FROM risaacson/erlang:18.1  
MAINTAINER Richard Isaacson <richard.c.isaacson@gmail.com>  
  
ENV ELIXIR_VERSION v1.1.1  
ADD https://github.com/elixir-lang/elixir/archive/${ELIXIR_VERSION}.tar.gz
/usr/src/  
  
run cd /usr/src \  
&& tar xf ${ELIXIR_VERSION}.tar.gz \  
&& cd elixir-${ELIXIR_VERSION#v} \  
&& LANG="en_US.UTF-8" make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/${ELIXIR_VERSION}.tar.gz
/usr/src/elixir-${ELIXIR_VERSION#v}  
  
CMD ["iex"]  

