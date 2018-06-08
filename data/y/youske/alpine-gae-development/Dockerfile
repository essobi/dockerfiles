# Alpine Linux miniconda with google_appengine sdk  
FROM youske/alpine-conda:latest  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
ENV LANG=C.UTF-8  
ENV APPENGINE_VERSION=1.9.38  
ENV SDK=https://storage.googleapis.com/appengine-
sdks/featured/google_appengine_${APPENGINE_VERSION}.zip  
  
ENV PACKAGE="unzip git tmux " \  
BUILD_PACKAGE="build-base python-dev musl-dev linux-headers" \  
LANGUAGE=${LANG} \  
TARGETDIR=/google_appengine \  
WORK=/home/admin/projects \  
PORT=8080-8089 \  
PATH=${TARGETDIR}:${PATH}  
  
# targetdir /google_appengine  
RUN apk update --no-cache && apk upgrade --no-cache && \  
apk add ${PACKAGE} \--no-cache && apk add ${BUILD_PACKAGE} \--no-cache -t
buildpack  
  
RUN wget -q ${SDK} -O /tmp/gae.zip && unzip -q /tmp/gae.zip -d /tmp/gtemp &&
mv /tmp/gtemp/google_appengine /google_appengine  
  
COPY requirements.txt /tmp  
RUN cd /tmp && pip install -U -r requirements.txt  
  
# remove buildpack  
RUN apk del buildpack --no-cache && rm -rf /tmp/* /var/cache/apk/*  
  
USER admin  
COPY notes/ /home/admin/notes  
  
EXPOSE ${PORT}  
  
USER root  
WORKDIR ${WORK}  
ENTRYPOINT ["switch","shell=su admin -c
/bin/bash","--","switch","root=/bin/bash","--","/init"]  
CMD ["su","admin","-c","/bin/bash"]  

