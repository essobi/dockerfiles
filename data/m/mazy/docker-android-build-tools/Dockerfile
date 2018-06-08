FROM georgepapas/docker-android-sdk:latest  
  
MAINTAINER Dmitry Rubtsov "dmitry@rubtsov.eu"  
# Forked from George Papastamatopoulos "george.papas@gmail.com"  
  
ENV ANDROID_BUILD_TOOLS_VERSION 25.0.1  
ENV DROID_XTRA extra-android-m2repository,extra-android-support,extra-
google-m2repository  
ENV DROID_TOOLS platform-tools,tools,build-
tools-${ANDROID_BUILD_TOOLS_VERSION}  
ENV DROID_API_LEVELS android-25  
ENV FILTER ${DROID_XTRA},${DROID_TOOLS},${DROID_API_LEVELS}  
RUN echo y | android update sdk -u -a -n && \  
echo y | android update sdk -u -a --filter ${FILTER}  
  
CMD ["bash"]  

