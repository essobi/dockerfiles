FROM trumhemcut/aspnet-fast  
  
MAINTAINER Phi Huynh <trumhemcut@gmail.com>  
  
RUN printf "deb http://ftp.us.debian.org/debian jessie main\n" >>
/etc/apt/sources.list  
RUN apt-get -qq update && apt-get install -qqy sqlite3 libsqlite3-dev && rm
-rf /var/lib/apt/lists/*  
  
COPY . /app  
WORKDIR /app/Kodj.Service  
RUN ["dnu", "restore"]  
WORKDIR /app/Kodj.Api  
RUN ["dnu", "restore"]  
RUN ["dnx", "ef", "database", "update"]  
  
EXPOSE 5000/tcp  
ENTRYPOINT ["dnx", "-p", "project.json", "web"]  

