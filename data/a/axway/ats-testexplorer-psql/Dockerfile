FROM ubuntu  
  
WORKDIR /app  
  
USER root  
  
RUN adduser --disabled-password atsuser  
  
RUN echo "atsuser:atspassword" | chpasswd  
  
RUN usermod -a -G sudo atsuser  
  
ADD ./docker_files /home/atsuser/app  
  
RUN apt-get update && apt-get -y install postgresql postgresql-client sudo
wget unzip openjdk-8-jdk-headless lsof nano ruby  
  
RUN ["chmod", "+x", "/home/atsuser/app/get_latest_te_files.rb"]  
RUN ["chmod", "+x", "/home/atsuser/app/get_latest_httpdblogger_files.rb"]  
RUN ["chmod", "+x", "/home/atsuser/app/run"]  
RUN ["chmod", "+x", "/home/atsuser/app/entrypoint"]  
  
RUN /home/atsuser/app/run  
  
EXPOSE 8080 5432  
  
USER atsuser  
  
ENTRYPOINT ["bash","-c", "/home/atsuser/app/entrypoint"]  
  

