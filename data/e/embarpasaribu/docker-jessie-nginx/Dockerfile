FROM embarpasaribu/docker-jessie:8.6  
WORKDIR /home/jessie/www  
  
EXPOSE 80  
RUN sudo sh -c "echo 'deb http://nginx.org/packages/debian jessie nginx' >
/etc/apt/sources.list.d/nginx.list" && \  
sudo sh -c "apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62" && \  
sudo apt-get update && \  
sudo apt-get install -y nginx  

