FROM debian  
CMD ["/bin/bash"]  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* && apt-get clean  

