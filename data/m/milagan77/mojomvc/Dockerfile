FROM hypriot/image-builder  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libsqlite3-dev \  
libzmq3-dev \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L https://cpanmin.us | perl - App::cpanminus  
  
RUN cpanm Mojolicious \  
&& cpanm Mojolicious::Plugin::OpenAPI \  
&& cpanm DBI \  
&& cpanm DBD::SQLite \  
&& cpanm ZMQ::LibZMQ3 \  
&& cpanm MojoX::Log::Log4perl \  
&& rm -fr ./cpanm /root/.cpanm /usr/src/perl /tmp/*  
  
COPY . /app  
  
WORKDIR /app  
  
RUN chmod a+x docker-entrypoint.sh  
  
EXPOSE 80/tcp  
  
CMD ["./docker-entrypoint.sh"]

