FROM hoborg/ubuntu-dev-base  
  
ARG PROXY=''  
  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
USER root  
  
RUN add-apt-repository ppa:jonathonf/python-3.6  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends --allow-unauthenticated
python3.6  
  
USER $USER  
  
COPY ./requirements-2.7.txt $HOME/requirements-2.7.txt  
COPY ./requirements-3.6.txt $HOME/requirements-3.6.txt  
COPY ./build.sh $HOME/build.sh  
RUN sudo chown -R "$USER":"$USER" $HOME  
# Create virtualenvs  
RUN ~/build.sh  
RUN rm ~/build.sh  
  
CMD ["/bin/zsh"]  

