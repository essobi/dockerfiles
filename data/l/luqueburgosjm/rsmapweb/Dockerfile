# SO  
FROM ubuntu:14.04  
# Autor  
MAINTAINER José Manuel Luque <luqueburgosjm@gmail.com>  
  
# Update y esenciales  
RUN sudo apt-get update  
RUN sudo apt-get install -y git  
RUN sudo apt-get install -y build-essential  
  
# Descaga repositorio  
RUN sudo git clone https://github.com/luqueburgosjm/RSMapWeb.git  
  
# Despliegue e instalacion  
RUN ls -l  
RUN cd RSMapWeb && make docker  
  
# Comando para lanzar la aplicacion  
CMD cd RSMapWeb && make run  

