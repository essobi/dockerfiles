FROM alpine:3.7  
LABEL maintainer='thomas.yager-madden@adops.com'  
# Install python3  
# Not using python:3-alpine to avoid  
# psycopg2 starting a separate python3 install  
RUN apk add --no-cache python3 py3-psycopg2  
  
# Copy in the code  
COPY *.py /app/  
COPY nerium/ /app/nerium/  
  
WORKDIR /app  
# Avoid breaking setup.py by adding this readme  
RUN touch /app/README.md  
# install from code currently in repo  
RUN pip3 install -e .  
# add jinjasql as a separate dependency instead  
RUN pip3 install jinjasql>=0.1.7  
VOLUME /app/query_files  
EXPOSE 8080  
CMD nerium

