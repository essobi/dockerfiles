# docker run --env-file env example  
FROM ruby:latest  
MAINTAINER henning mueller <mail@nning.io>  
  
RUN useradd -m ruby  
  
USER ruby  
WORKDIR home/ruby  
ADD . review_nagger  
  
USER root  
RUN chown -R ruby:ruby review_nagger  
  
USER ruby  
WORKDIR review_nagger  
RUN bundle  
  
CMD ruby bin/review_nagger  

