FROM perl:5  
# Install sqitch and required dependencies  
RUN apt-get update \  
&& apt-get install --yes --auto-remove --no-install-recommends \  
libdbd-pg-perl postgresql-client sqitch \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["sqitch"]  
CMD ["--help"]  

