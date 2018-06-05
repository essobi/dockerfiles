FROM codenvy/android  
  
RUN sudo apt-get update && \  
sudo apt-get install -y -q build-essential curl git ruby zlib1g-dev libssl-dev
\  
libreadline-dev libyaml-dev libxml2-dev libxslt-dev ruby-dev libffi-dev  
  
RUN echo 'PATH=~/android-sdk-linux/platform-tools/:~/android-sdk-
linux/tools/:$PATH' >> ~/.bashrc  
  
# install cloud9  
RUN git config --global url."https://".insteadOf git:// && \  
git clone git://github.com/c9/core.git c9sdk &&\  
cd c9sdk &&\  
scripts/install-sdk.sh  
  
# Tweak standlone.js conf  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /home/user/c9sdk/configs/standalone.js  
  
RUN echo 'C9_DIR=$HOME/.c9' >> .bashrc  
RUN echo 'PATH=$C9_DIR/node/bin:$PATH' >> .bashrc  
  
ADD conf/cloud9.conf /opt/cloud9.conf  
USER root  
RUN cat /opt/cloud9.conf >> /opt/supervisord.conf  
  
USER user  
#manymo  
RUN curl https://raw.githubusercontent.com/manymo/manymo/master/manymo-
installer | bash  
  
VOLUME /workspace  
  
EXPOSE 8080  

