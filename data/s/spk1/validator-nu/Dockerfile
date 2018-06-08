FROM java:openjdk-8-jre  
MAINTAINER Laurent Arnoud <laurent@spkdev.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBIAN_PRIORITY critical  
ENV DEBCONF_NOWARNINGS yes  
  
ENV VALIDATOR_NU_VERSION 17.3.0  
ENV VALIDATOR_NU_SHA256
12d9baab16c08daa142a50ad368f3906e1aa460dc993a7f2124f003366c590aa  
ENV VALIDATOR_NU_PORT 8888  
ENV VALIDATOR_NU_ZIP vnu.jar_${VALIDATOR_NU_VERSION}.zip  
ENV VALIDATOR_NU_URL
https://github.com/validator/validator/releases/download/${VALIDATOR_NU_VERSION}/${VALIDATOR_NU_ZIP}  
ENV VALIDATOR_NU_DEST /opt  
  
RUN apt-get update -qq \  
&& apt-get -y --no-install-recommends install unzip \  
&& apt-get purge -y \  
&& apt-get autoremove -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ${VALIDATOR_NU_URL} /tmp  
RUN unzip -d ${VALIDATOR_NU_DEST} /tmp/${VALIDATOR_NU_ZIP} \  
&& echo "${VALIDATOR_NU_SHA256} /tmp/${VALIDATOR_NU_ZIP}" | sha256sum -c - \  
&& apt-get -y remove --purge unzip && rm -rf /tmp/*  
  
USER nobody  
WORKDIR ${VALIDATOR_NU_DEST}/dist  
CMD ["java", "-cp", "vnu.jar", "nu.validator.servlet.Main", "8888"]  
  
EXPOSE ${VALIDATOR_NU_PORT}  

