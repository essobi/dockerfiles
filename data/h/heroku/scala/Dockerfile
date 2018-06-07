# Inherit from Heroku's stack  
FROM heroku/jvm  
  
# Install sbt-extras  
RUN mkdir -p /app/bin  
ADD ./sbt-extras.sh /app/bin/sbt  
RUN chmod +x /app/bin/sbt  
ENV PATH /app/bin:$PATH  
  
# Run sbt-extras to make sure the sbt version is downloaded and cached  
ONBUILD COPY project/build.properties /app/user/project/  
ONBUILD RUN sbt about  
  
# Run sbt update to make sure the dependencies are downloaded and cached  
ONBUILD COPY ["*.sbt", "*.scala", "/app/user/"]  
ONBUILD COPY ["project/*.sbt", "project/*.scala", "/app/user/project/"]  
ONBUILD RUN rm -f project/play-fork-run.sbt  
ONBUILD RUN sbt clean update  
  
ONBUILD COPY . /app/user/  
ONBUILD RUN rm -f project/play-fork-run.sbt  
ONBUILD RUN rm -f target/universal/stage/RUNNING_PID  
ONBUILD RUN sbt stage  
  
COPY ./init.sh /usr/bin/init.sh  
RUN chmod +x /usr/bin/init.sh  
ENTRYPOINT ["/usr/bin/init.sh"]  

