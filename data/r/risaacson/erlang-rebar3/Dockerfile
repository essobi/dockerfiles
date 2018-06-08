FROM risaacson/erlang:18.1  
MAINTAINER Richard Isaacson <richard.c.isaacson@gmail.com>  
  
ENV REBAR3_VERSION 3.0.0-beta.3  
#ADD https://github.com/rebar/rebar3/archive/${REBAR_VERSION}.tar.gz
/usr/src/rebar-${REBAR_VERSION}.tar.gz  
RUN cd /usr/src \  
&& git clone \--branch ${REBAR3_VERSION} https://github.com/rebar/rebar3.git \  
&& cd rebar3 \  
&& ./bootstrap \  
&& cp rebar3 /usr/bin/rebar3 \  
&& cd / && rm -rf /usr/src/rebar3  
  
#RUN cd /usr/src \  
# && tar zxf rebar-${REBAR_VERSION}.tar.gz \  
# && cd rebar3-${REBAR_VERSION} \  
# && ./bootstrap \  
# && cp rebar3 /usr/bin/rebar \  
# && cd / && rm -rf /usr/src/rebar-${REBAR_VERSION}  
CMD ["erl"]  

