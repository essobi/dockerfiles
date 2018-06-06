FROM alpine:edge  
STOPSIGNAL 9  
HEALTHCHECK CMD curl -f http://localhost:5000/ || exit 1  
  
RUN apk update && apk upgrade  
RUN apk add curl wget perl-dev perl make gcc git subversion tzdata libc-dev
docker bash curl wget perl-dev perl make gcc git tzdata libc-dev docker
openssh-client  
  
RUN curl -L https://cpanmin.us | perl - App::cpanminus  
  
RUN cpanm --force -n Dancer2 Plack::Middleware::Deflater
Dancer2::Template::TemplateToolkit \  
Switch \  
Dancer2::Plugin::Auth::Extensible \  
Dancer2::Plugin::Auth::Extensible::Provider::LDAP \  
File::Slurper \  
DBD::SQLite \  
Dancer2::Plugin::Database  
  
ENV TZ Europe/Berlin  
EXPOSE 5000  
WORKDIR /app  
CMD ["/usr/bin/perl", "/usr/local/bin/plackup", "-r", "/app/bin/app.psgi"]  

