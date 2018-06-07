FROM ubuntu:xenial  
RUN apt-get update  
RUN apt-get -y install curl apt-utils git expect dos2unix  
#RUN apt-get -y install git gcc g++ php python r-base sqlite3 mono-complete
openjdk-8-jdk  
COPY prep_env.sh /prep_env.sh  
COPY clone_repo.sh /clone_repo.sh  
COPY pkg_installer.sh /pkg_installer.sh  
COPY init.sh /init.sh  
COPY update_repo.sh /update_repo.sh  
  
RUN dos2unix /clone_repo.sh  
RUN dos2unix /prep_env.sh  
RUN dos2unix /pkg_installer.sh  
RUN dos2unix /init.sh  
RUN dos2unix /update_repo.sh  
  
RUN expect /clone_repo.sh  
RUN bash /pkg_installer.sh  
RUN bash /prep_env.sh  
EXPOSE 1789 80  
ENTRYPOINT ["bash", "/init.sh"]

