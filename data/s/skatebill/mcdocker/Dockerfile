FROM skatebill/mcdocker  
  
#RUN mkdir /app/mods/  
ADD . /app/mods/  
RUN bash build.sh  
#WORKDIR /app  
  
#RUN mkdir mods/.minecrft  
#RUN mkdir mods/.minecrft/mods  
#RUN mkdir client  
#RUN tar xf /usr/local/tomcat/webapps/ROOT/client.tar -C client/  
#RUN mkdir client/.minecraft/mods  
#RUN rm client.tar  
#RUN cp mods/client/* client/.minecraft/mods/  
#RUN cp mods/universal/* client/.minecraft/mods/  
#RUN cp mods/universal/* server/mods/  
#RUN tar cf client.tar client  
#RUN mv client.tar /usr/local/tomcat/webapps/ROOT/  
#RUN rm -rf mods  
#RUN rm -rf client  
  
  
# Make port 80 available to the world outside this container  
#EXPOSE 8080  
#EXPOSE 25565  
#/usr/local/tomcat/webapps/ROOT  
  
CMD ["bash","run.sh"]

