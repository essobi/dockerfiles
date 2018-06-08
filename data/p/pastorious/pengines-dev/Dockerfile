FROM ubuntu:xenial  
RUN echo '\n\ndeb http://ppa.launchpad.net/swi-prolog/devel/ubuntu xenial
main\ndeb-src http://ppa.launchpad.net/swi-prolog/devel/ubuntu xenial main' >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys
73E75048FF27533C0D8DC521EF8406856DBFCA18  
RUN apt-get update && apt-get install -y git swi-prolog  
RUN git clone https://github.com/SWI-Prolog/pengines  
# Expose the default port for pengines  
EXPOSE 3030  
# Set the pengines admin account to admin:admin  
RUN echo 'admin:$1$vUXiHMJy$DI1JHDLqTytUYGTHicJvE0' >>/pengines/passwd  
WORKDIR /pengines  
ENTRYPOINT ["swipl"]  
CMD ["daemon.pl","--port=3030","--fork=false"]  

