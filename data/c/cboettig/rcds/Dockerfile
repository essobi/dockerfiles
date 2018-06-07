FROM rocker/verse:3.3.1  
RUN apt-get update && apt-get -y install --no-install-recommends jekyll ruby-
rouge  
  
WORKDIR /home/rstudio  
EXPOSE 4000  
ENV SERVE TRUE  
  
CMD Rscript -e "dirs = c('.', 'readings', 'assignments', 'lectures');
servr::jekyll('website', serve=$SERVE, input = dirs, output = dirs, host =
'0.0.0.0', port=4000)"  
  
## Build & view site on localhost:  
# docker run -d -p 4000:4000 -v $(pwd):/home/rstudio cboettig/rcds  
## Build site into docs/  
# docker run -ti -v $(pwd):/home/rstudio -e SERVE=FALSE cboettig/rcds  

