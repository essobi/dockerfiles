FROM tooit/docker-nginx-drupal  
  
ADD ./facedetect /usr/local/bin/facedetect  
  
RUN sudo apt-get update; \  
sudo apt-get -y install wget unzip python python-opencv libopencv-dev python-
numpy; \  
sudo chmod +x /usr/local/bin/facedetect  
  

