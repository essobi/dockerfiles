FROM node  
  
## Base packages  
RUN apt-get update -qq && apt-get upgrade -y -qq  
RUN apt-get install -qq -y curl  
RUN apt-get install -y wget  
######  
#  
RUN curl https://install.meteor.com/ | sh  
RUN npm install -g meteorite  
  
RUN git clone https://github.com/TelescopeJS/Telescope.git /src && mrt update  
  
WORKDIR /src  
  
ADD run.sh /root/bin/run.sh  
RUN chmod +x /root/bin/run.sh  
  
# Create a /data folder  
RUN mkdir /data  
# This is weird but working, even when mounting a /data with -v  
RUN ln -s /src/.meteor/local/db /data/telescope  
  
EXPOSE 3000  
CMD ["/root/bin/run.sh"]  

