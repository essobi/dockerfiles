from microsoft/aspnet  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y vim  
  
  
RUN bash -c "source $DNX_USER_HOME/dnvm/dnvm.sh \  
&& dnvm upgrade"  
  
WORKDIR /app  
  
# Open this port in the container  
EXPOSE 5000  
  
#ENTRYPOINT ["dnx","-p","project.json", "web"]  
ENTRYPOINT ["/bin/bash"]  
  

