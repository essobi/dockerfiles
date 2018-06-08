FROM mxlab/ubuntu-base  
MAINTAINER Lacour Maxime <dockerhub@lacour-maxime.fr>  
  
RUN apt-get update && \  
apt-get install -y gearman-job-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 4730  
  
CMD ["gearmand", "-p 4730"]  

