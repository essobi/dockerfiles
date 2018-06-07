FROM postgres  
  
ENV POSTGRES_USER concourse  
ENV POSTGRES_PASSWORD concourse  
ENV POSTGRES_DB concourse  
  
RUN apt-get update && apt-get install -y supervisor curl  
  
RUN curl -s -L -o /usr/local/bin/concourse
https://github.com/concourse/concourse/releases/download/v3.3.4/concourse_linux_amd64  
  
RUN chmod +x /usr/local/bin/concourse  
  
EXPOSE 5432 8080  
ADD supervisor /etc/supervisor/conf.d  
ADD scripts/ /concourse  
ADD keys/ /concourse/keys/  
  
RUN mkdir /concourse/logs /concourse/workdir  
  
VOLUME /concourse/workdir  
  
CMD ["supervisord", "-n"]  

