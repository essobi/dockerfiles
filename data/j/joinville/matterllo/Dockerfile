FROM python:2  
ENV APP_ROOT /usr/src/app  
  
# We are using a specific matterllo version (commit):  
# the last using YAML config file instead of a database.  
ENV MATTERLLO_VERSION 85ef4d2fb654499079a33326166146dbcd134f37  
RUN git clone https://github.com/Lujeni/matterllo.git $APP_ROOT && \  
cd $APP_ROOT && \  
git reset --hard $MATTERLLO_VERSION  
  
# Install all required Python modules  
RUN pip install --no-cache-dir -r $APP_ROOT/requirements.txt  
  
# Must set PYTHONPATH so 'import matterllo.utils' works  
ENV PYTHONPATH $APP_ROOT  
  
ENV MATTERLLO_CONFIG_FILE $APP_ROOT/config.yaml  
ENV MATTERLLO_API_HOST 0.0.0.0  
# Port is fixed, because setting $MATTERLLO_API_PORT raises error  
EXPOSE 8080  
WORKDIR $APP_ROOT  
ENTRYPOINT [ "python", "run.py" ]  

