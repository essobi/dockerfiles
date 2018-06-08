FROM python:3.5  
MAINTAINER Evan Zeimet <podnov@gmail.com>  
  
RUN useradd -m prom2teams  
  
RUN pip3 install prom2teams --no-cache-dir  
  
COPY Dockerfile /Dockerfile  
  
COPY prom2teams.ini /home/prom2teams/prom2teams.ini  
RUN chown prom2teams:prom2teams /home/prom2teams/prom2teams.ini  
  
COPY prom2teams.sh /home/prom2teams/prom2teams.sh  
RUN chown prom2teams:prom2teams /home/prom2teams/prom2teams.sh  
RUN chmod +x /home/prom2teams/prom2teams.sh  
  
USER prom2teams  
  
ENV PROM2TEAMS_CONFIGPATH="/home/prom2teams/prom2teams.ini"  
ENV PROM2TEAMS_HOST="0.0.0.0"  
ENV PROM2TEAMS_PORT="8089"  
ENV PROM2TEAMS_LOGLEVEL="INFO"  
WORKDIR /home/prom2teams  
CMD /home/prom2teams/prom2teams.sh  
  
LABEL org.label-schema.docker.dockerfile="/prom2teams/Dockerfile" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/podnov/com.docker.hub"  

