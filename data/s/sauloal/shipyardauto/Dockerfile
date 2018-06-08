#TO BUILD SAULOAL/SHIPYARD  
#docker run --privileged -it --name dockerindocker -v
$PWD/data:/var/lib/docker jpetazzo/dind  
# docker run -i -t -v /var/run/docker.sock:/docker.sock shipyard/deploy setup  
#docker commit -a "Saulo Alves <sauloal@gmail.com>" dockerindocker
sauloal/shipyard  
#  
#TO BUILD SAULOAL/SHIPYARDAUTO  
#docker build -t sauloal/shipyardauto .  
FROM sauloal/shipyard  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  
  

