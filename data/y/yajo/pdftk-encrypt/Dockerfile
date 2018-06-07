# -*- coding: utf-8 -*-  
# © 2015 Grupo ESOC Ingeniería de Servicios, S.L.U. - Jairo Llopis  
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).  
FROM debian  
MAINTAINER Jairo Llopis <yajo.sk8@gmail.com>  
  
RUN apt-get update &&\  
apt-get -y install pdftk &&\  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y  
  
ENV OWNER_PW=owner USER_PW=user  
CMD pdftk - output - owner_pw $OWNER_PW user_pw $USER_PW  

