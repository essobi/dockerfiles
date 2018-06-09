FROM phusion/passenger-nodejs  
  
RUN apt-get update && apt-get install -y \  
curl \  
git  
  
RUN curl https://install.meteor.com/ | sh && git clone
https://github.com/TelescopeJS/Telescope.git /telescope  
  
WORKDIR /telescope  
  
COPY run.sh /bin/  
  
EXPOSE 3000  
CMD ["sh", "/bin/run.sh"]  

