FROM alpine:latest  
MAINTAINER Borodin Gregory <grihabor@mail.ru>  
  
WORKDIR /server  
  
ADD IntelliJIDEALicenseServer_linux_amd64 ./pycharm_activation_server  
RUN chmod +x pycharm_activation_server  
  
EXPOSE 1017  
CMD ./pycharm_activation_server  

