FROM netflixoss/java:8  
MAINTAINER Jose Armesto <jose@armesto.net>  
  
EXPOSE 8080  
ADD build/install/turbine /code  
ENTRYPOINT ["/code/bin/turbine"]  
CMD ["com.scmspain.turbine.Application"]

