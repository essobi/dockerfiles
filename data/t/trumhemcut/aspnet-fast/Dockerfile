FROM microsoft/aspnet  
  
RUN printf "deb http://ftp.us.debian.org/debian jessie main\n" >>
/etc/apt/sources.list  
RUN apt-get -qq update && apt-get install -qqy sqlite3 libsqlite3-dev && rm
-rf /var/lib/apt/lists/*  
  
COPY project.json /package_profiles/  
WORKDIR /package_profiles  
RUN ["dnu", "restore"]  

