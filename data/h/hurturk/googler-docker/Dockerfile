FROM python:3.4.7-slim  
RUN apt-get update -y && apt-get install curl links2 -y && rm -rf
/var/lib/apt/lists/*  
RUN curl -o /usr/local/bin/googler
https://raw.githubusercontent.com/jarun/googler/v3.4/googler && chmod +x
/usr/local/bin/googler  
RUN ln -s /usr/bin/links2 /usr/bin/links  
ENV BROWSER links  
ENTRYPOINT ["/usr/local/bin/googler"]  
CMD ["-h"]  

