FROM alpine:latest  
  
ENV DOCKER_PARSER_VERSION=3.4.4  
ENV DOCKER_PARSER_MYSQL_VERSION=10.7  
  
RUN apk add \--no-cache \--virtual .builddeps tar bison gcc g++ linux-headers
make mariadb-dev \  
&& mkdir -p /src/sql 2>/dev/null && cd /src \  
&& wget
http://www.parser.ru/f/1/download/src/parser-$DOCKER_PARSER_VERSION.tar.gz -O-
| tar xz \  
&& cd /src/sql && wget
http://www.parser.ru/f/1/download/src/parser3mysql-$DOCKER_PARSER_MYSQL_VERSION.tar.gz
-O- | tar xz \  
&& mv /src/parser-$DOCKER_PARSER_VERSION /src/parser3 && cd /src/parser3 \  
&& sed -i 's/download="wget -c --passive-ftp"/download="wget -c"/' buildall \  
&& sed -i 's/CPPFLAGS="-DUSE_LIBC_PRIVATES -DUSE_MMAP
-DDONT_ADD_BYTE_AT_END"/CPPFLAGS="-DUSE_LIBC_PRIVATES -DUSE_MMAP
-DDONT_ADD_BYTE_AT_END -DNO_GETCONTEXT"/' buildall \  
&& sed -Ei 's/(typedef struct _fpstate|struct sigcontext)/\1_/'
/usr/include/bits/signal.h \  
&& ./buildall \--strip \  
&& cd /src/sql/parser3mysql-$DOCKER_PARSER_MYSQL_VERSION \  
&& ./configure \--prefix=/root/parser3install/bin && make && make install \  
&& mv /root/parser3install/bin /usr/local/parser3 && mv
/root/parser3install/share/charsets /usr/local/parser3 \  
&& cd / && rm -rf /src/* \  
&& apk del .builddeps && rm -f /tmp/*  
  
RUN apk add \--no-cache mariadb-client-libs libcurl fcgiwrap libstdc++ libgcc
\  
&& rm -rf /tmp/* \  
&& ln -s "$(ls -1 /usr/lib/libmysqlclient.so.* | head -1 | xargs basename)"
/usr/lib/libmysqlclient.so \  
&& ln -s "$(ls -1 /usr/lib/libcurl.so.* | head -1 | xargs basename)"
/usr/lib/libcurl.so  
  
ENV CGI_PARSER_LOG=/dev/stdout  
  
EXPOSE 9000  
  
USER nobody  
  
CMD ["fcgiwrap", "-f", "-c", "3", "-s", "tcp:0.0.0.0:9000"]  

