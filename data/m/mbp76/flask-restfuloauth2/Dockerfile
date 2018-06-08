FROM mbp76/docker-gradle  
MAINTAINER mbp76@users.noreply.github.com  
  
ADD . /home/builder  
WORKDIR /home/builder  
ENV FLASK_APP="restfuloauth2"  
ENV SECRET_KEY="non-production-key"  
CMD gradle --continuous  

