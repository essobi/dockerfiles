FROM nayibor/yaws_docker:0.1.0 as builder  
RUN apt-get update  
RUN apt-get install -y autoconf build-essential  
  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN rebar3 get-deps  
RUN rebar3 compile  
RUN ls -al  
WORKDIR /usr/src/app/_build/default/lib/yaws  
RUN /usr/bin/autoreconf -fi  
RUN ./configure --disable-pam  
RUN make  
WORKDIR /usr/src/app  
RUN rebar3 release -n erlmon_docker tar  
RUN mkdir -p /opt/rel  
RUN tar -xzf /usr/src/app/_build/default/rel/*/erlmon_docker*.tar.gz -C
/opt/rel  
RUN tar -xzf /usr/src/app/_build/default/rel/*/*.tar.gz -C /opt/rel  
  
FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends openssl unixodbc unixodbc-dev
freetds-dev tdsodbc telnet freetds-bin net-tools  
WORKDIR /opt/erl_monitor  
COPY odbcinst.ini /etc  
COPY odbc.ini /etc  
COPY freetds.conf /etc/freetds/  
#iptables -A INPUT -i mssql_server -j ACCEPT  
ENV RELX_REPLACE_OS_VARS true  
ENV EMAIL_HOST=""  
ENV EMAIL_USER=""  
ENV EMAIL_PASS=""  
ENV EMAIL_FROM_ADDRESS=""  
ENV DB_HOST=""  
ENV DB_USER=""  
ENV DB_PASS=""  
COPY \--from=builder /opt/rel /opt/erl_monitor  
EXPOSE 8004 8004  
EXPOSE 8002 8002  
ENTRYPOINT ["/opt/erl_monitor/bin/erlmon_docker"]  
  

