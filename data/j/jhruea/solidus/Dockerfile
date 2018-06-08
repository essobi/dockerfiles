FROM ruby  
  
## install node and postgres client  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-
client  
RUN apt-get install -y nodejs  
RUN rm -rf /var/lib/apt/lists/*  
  
## copy stubs to where they need to be  
COPY stubs/Gemfile-rails /tmp  
COPY stubs/Gemfile-solidus /tmp  
COPY stubs/site-database.yml /tmp  
  
## copy scripts to /bin and run installation script  
COPY scripts/inst_solidus.sh /bin  
COPY scripts/post_init.sh /bin  
COPY scripts/run_solidus.sh /bin  
RUN /bin/inst_solidus.sh  
  
## set WORKDIR and set command to start solidus  
WORKDIR /usr/src/app  
EXPOSE 3000  
CMD /bin/run_solidus.sh  

