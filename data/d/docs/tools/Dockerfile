FROM docs/docker.github.io:latest  
  
# Set to 1 to make the link checker log its status  
ENV DEBUG 0  
# Set to 0 to check $SITE. If 1, checks target/index.html inside the container  
ENV LOCAL 1  
# Set to 1 to follow and check external links  
ENV CHECKEXTERN 0  
# Set to a different URL to check that  
ENV SITE https://docs.docker.com  
  
# Add the wrapper script  
ADD linkchecker.sh linkchecker.sh  
ADD linkchecker.conf linkchecker.conf  
  
RUN apt-get update && apt-get install -q -y --no-install-recommends python-
requests ca-certificates linkchecker  
  
CMD PYTHONWARNINGS="ignore:Unverified HTTPS request" ./linkchecker.sh

