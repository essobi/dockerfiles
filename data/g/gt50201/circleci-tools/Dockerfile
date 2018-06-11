FROM python:2.7.14-slim  
  
USER root  
  
RUN useradd --create-home circleci  
RUN mkdir /home/circleci/tools  
COPY ./cancel_prior_builds.py /home/circleci/tools/  
RUN chown circleci:circleci -R /home/circleci/tools/  
  
USER circleci  
WORKDIR /home/circleci  
  
  

