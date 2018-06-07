FROM youyo/development:latest  
ENV ERLANG_VERSION 18.0  
WORKDIR /usr/local/src/  
RUN wget http://www.erlang.org/download/otp_src_${ERLANG_VERSION}.tar.gz  
RUN tar xvzf otp_src_${ERLANG_VERSION}.tar.gz  
WORKDIR /usr/local/src/otp_src_${ERLANG_VERSION}  
RUN ./configure  
RUN make  
RUN make install  
RUN rm -rf /usr/local/src/*  
RUN erl -version  

