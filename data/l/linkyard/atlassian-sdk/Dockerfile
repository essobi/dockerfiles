FROM java:8-jdk  
LABEL maintainer="mario.siegenthaler@linkyard.ch"  
  
# Add Tini  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Prepare for sdk installation  
RUN apt-get -y update \  
&& apt-get -y install apt-transport-https  
  
ENV SDK_VERSION=6.3.6  
# Install atlassian sdk  
RUN echo "deb http://sdkrepo.atlassian.com/debian/ stable contrib"
>>/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B07804338C015B73 \  
&& apt-get -y update \  
&& apt-get -y install atlassian-plugin-sdk=${SDK_VERSION}  
  
RUN mkdir -p /app  
WORKDIR /app  
  
EXPOSE 2990  
EXPOSE 5005  
CMD ["atlas-version"]  

