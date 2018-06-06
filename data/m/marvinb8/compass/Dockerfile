FROM debian:jessie  
  
ENV working_dir /app  
  
WORKDIR ${working_dir}  
  
RUN apt-get update && \  
apt-get install ruby-dev -y && \  
apt-get install ruby-full ruby-sass ruby-compass rubygems -y  
CMD ["compass"]  

