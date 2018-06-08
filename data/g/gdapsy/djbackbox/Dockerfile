# vim:set ft=dockerfile:  
FROM gdapsy/baseansibbox  
RUN apt-get update  
RUN apt-get upgrade -y  
ADD books /home/root/books  
RUN ansible-playbook -i /home/root/books/inventory/hosts
/home/root/books/devbook/main.yml  
  
  
  

