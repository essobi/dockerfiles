# Create a base docker container that will run FSL's FEAT  
#  
#  
FROM neurodebian:xenial  
MAINTAINER Flywheel <support@flywheel.io>  
  
  
# Install dependencies  
RUN echo deb http://neurodeb.pirsquared.org data main contrib non-free >>
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN echo deb http://neurodeb.pirsquared.org xenial main contrib non-free >>
/etc/apt/sources.list.d/neurodebian.sources.list  
RUN apt-get update \  
&& apt-get install -y \  
fsl-5.0-complete \  
zip \  
jq \  
lsb-core \  
curl \  
bsdtar \  
python-pip  
  
# Download/Install webpage2html  
ENV COMMIT=4dec20eba862335aaf1718d04b313bdc96e7dc8e  
ENV URL=https://github.com/zTrix/webpage2html/archive/$COMMIT.zip  
RUN curl -#L $URL | bsdtar -xf- -C /opt/  
WORKDIR /opt  
RUN mv webpage2html-$COMMIT webpage2html  
RUN pip install -r webpage2html/requirements.txt  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
COPY template.fsf ${FLYWHEEL}/  
  
# Configure entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  

