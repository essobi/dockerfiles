# Image to create todo milestones in Gitlab  
FROM seetheprogress/ubuntu:14.04  
MAINTAINER Michael Grosser <docker@stp-ip.net>  
  
# ENVs can be provided via ENV files inside the config and secrets dir.  
# Following mandatory ENVs will be used:  
# GITLAB_API_URL, GITLAB_API_KEY, GITLAB_NAMESPACE, GITLAB_PROJECT  
# Following optional ENVs will be used, if provided:  
# MILESTONE_ADVANCE  
# Disable specific mount checks  
ENV CHECK_LOG false  
ENV CHECK_DATA false  
  
# ENVs for easier editing  
# Source code  
ENV GITLAB_TODO_VERSION v0.9.1  
ENV GITLAB_TODO_SOURCE https://dev.seetheprogress.eu/stp/gitlab_todo.git  
  
# Verification  
ENV KEY_ID A84D05A2  
ENV FINGERPRINT AA22 711B 01FF 2A34 4065 11F2 2EA6 6081 CE13 1AE8  
  
# Dependencies  
ENV REQUESTS_VERSION 2.5.0  
ENV ARGPARSE_VERSION 1.2.2  
# Default advance  
ENV MILESTONE_ADVANCE 30  
# User specifics  
# Do not edit during "run"  
ENV CONTAINER_USER gitlab_todo  
ENV CONTAINER_GROUP gitlab_todo  
  
# Add user and group  
RUN groupadd -r $CONTAINER_GROUP  
RUN useradd -m -g $CONTAINER_GROUP -b /home/ -s /sbin/nologin $CONTAINER_USER  
  
# Clean system to prevent false python version  
RUN apt-get purge -y python.*  
  
# Use System Python for now  
# TODO: Setup specific Python version  
RUN apt-get update \  
&& apt-get install -y \  
python3 \  
python3-pip \  
# Install git until build containers are supported  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setup Python deps  
RUN pip3 install argparse==$ARGPARSE_VERSION  
RUN pip3 install requests==$REQUESTS_VERSION  
  
# Install gitlab_todo from source  
# Get code directly in container until build containers are supported  
RUN mkdir -p /con/context/src \  
&& cd /con/context/src/ \  
&& git clone $GITLAB_TODO_SOURCE \  
&& cd gitlab_todo \  
&& git fetch --all \  
&& git checkout tags/$GITLAB_TODO_VERSION  
  
COPY context/entrypoint.sh /con/context/entrypoint.sh  
RUN chmod +x /con/context/entrypoint.sh  
  
# Set permissions to gitlab_todo  
RUN chown -R $CONTAINER_USER:$CONTAINER_GROUP /con/*  
  
USER $CONTAINER_USER  
  
ENTRYPOINT ["/con/context/entrypoint.sh"]  
  
CMD python3 \  
/con/context/src/gitlab_todo/gitlab_todo.py \  
\--namespace=$GITLAB_NAMESPACE \  
\--project=$GITLAB_PROJECT \  
\--api_key=$GITLAB_API_KEY \  
\--api_base=$GITLAB_API_URL \  
\--advance=$MILESTONE_ADVANCE  

