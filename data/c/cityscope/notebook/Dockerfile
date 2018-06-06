FROM jupyter/singleuser  
  
USER jovyan  
  
RUN pip install -e git://github.com/python-
visualization/folium.git@8fa74b90d69a0caff125c4de45c977b6d8b73ca4#egg=folium  
  
USER root  
RUN apt-get update && apt-get install -y \  
mysql-client  
ADD singleuser-cityscope.sh /srv/singleuser/singleuser-cityscope.sh  
  
USER jovyan  
CMD ["sh", "/srv/singleuser/singleuser-cityscope.sh"]  

