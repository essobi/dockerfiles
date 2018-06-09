FROM ubuntu  
RUN apt-get update -qq \  
&& apt-get --no-install-recommends -qq --no-install-recommends --no-install-
suggests install stress-ng \  
&& rm -rf /var/lib/apt/lists/*  
  
entrypoint ["stress-ng"]  

