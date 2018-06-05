FROM vertx/vertx3  
  
#  
ENV VERTICLE_NAME de.comhix.anime.ServerBase  
ENV VERTICLE_FILE api.jar  
  
# Set the location of the verticles  
ENV VERTICLE_HOME /usr/verticles  
  
EXPOSE 8080  
# Copy your verticle to the container  
COPY $VERTICLE_FILE $VERTICLE_HOME/  
  
RUN mkdir $VERTICLE_HOME/lib  
COPY lib/* $VERTICLE_HOME/lib/  
  
RUN mkdir $VERTICLE_HOME/data  
  
# Launch the verticle  
WORKDIR $VERTICLE_HOME  
ENTRYPOINT ["sh", "-c"]  
#CMD ["exec vertx run $VERTICLE_NAME -cp $VERTICLE_HOME/*"]  
CMD ["exec java -jar $VERTICLE_FILE"]

