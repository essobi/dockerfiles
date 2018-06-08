FROM python:slim  
MAINTAINER rogeriopradoj@gmail.com  
  
ENV GITHUB_TOKEN=update_accordingly  
  
RUN apt-get update && apt-get install git -y  
  
RUN pip install octohatrack  
  
WORKDIR /cache  
  
ENTRYPOINT ["octohatrack"]  
CMD ["-h"]  

