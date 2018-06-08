FROM dockerfile/java:oracle-java7  
  
# Set up app directory.  
ONBUILD USER root  
ONBUILD ADD . $APP_PATH  
ONBUILD RUN chown -R $DEV_USER:$DEV_GROUP $APP_PATH  
ONBUILD USER $DEV_USER  
ONBUILD RUN lein install && lein clean  
  
ENV DEV_USER dev  
ENV DEV_GROUP staff  
ENV HOME /home/$DEV_USER  
ENV APP_PATH /app  
  
# Set up user  
RUN useradd $DEV_USER -g 50 -G $DEV_GROUP -u 1000 -s /bin/bash --create-home  
  
# Install Python.  
RUN apt-get update \  
&& apt-get install -y python \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Storm  
ENV STORM_VERSION 0.8.0  
RUN wget -q -o /tmp/storm-$STORM_VERSION.zip \  
https://s3.amazonaws.com/promojam-
devops/packages/storm/storm-$STORM_VERSION.zip \  
&& unzip -o storm-$STORM_VERSION.zip -d /usr/local/share \  
&& ln -s /usr/local/share/storm-$STORM_VERSION /usr/local/share/storm \  
&& ln -s /usr/local/share/storm/bin/storm /usr/bin/storm \  
&& rm /tmp/storm-$STORM_VERSION.zip  
  
# Install Leiningen  
ENV LEIN_VERSION 2.4.3  
RUN wget -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/$LEIN_VERSION/bin/lein
\  
&& chmod +x /usr/bin/lein  
USER $DEV_USER  
RUN lein  
USER root  
  
RUN mkdir -p $APP_PATH \  
&& chown -R $DEV_USER $APP_PATH \  
&& mkdir $HOME/.storm \  
&& chown -R $DEV_USER $HOME/.storm  
  
USER $DEV_USER  
  
VOLUME [$APP_PATH]  
CMD ["bash"]  
  
WORKDIR $APP_PATH  

