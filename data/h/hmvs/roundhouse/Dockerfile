# Set the base image  
FROM mono:5.8.0.108  
# Dockerfile author / maintainer  
MAINTAINER Vadym Kurachevskyi <vadim@hmvs.org>  
  
RUN mkdir /rh  
WORKDIR /rh  
  
RUN nuget install -NonInteractive -Version 0.9.1 roundhouse  
  
ADD rh.exe.config /rh/roundhouse.0.9.1/tools/rh.exe.config  
  
WORKDIR /rh/roundhouse.0.9.1/tools/  
  
ENTRYPOINT ["mono", "rh.exe"]  
  
CMD ["--help"]  

