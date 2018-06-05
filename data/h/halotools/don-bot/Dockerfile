# Get the halocelery component  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4 as downloader  
MAINTAINER toolbox@cloudpassage.com  
  
ARG HALOCELERY_BRANCH=feature/CS-546  
RUN apt-get update && \  
apt-get install -y \  
git  
  
WORKDIR /app/  
  
RUN echo "Target branch for this build: $HALOCELERY_BRANCH"  
  
RUN git clone -b $HALOCELERY_BRANCH https://github.com/cloudpassage/halocelery  
  
RUN cd halocelery && \  
git archive \  
\--verbose \  
\--format=tar.gz \  
-o /app/halocelery.tar.gz \  
$HALOCELERY_BRANCH  
  
#####################################  
# Unit and integration tests run in a separate step.  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4  
MAINTAINER toolbox@cloudpassage.com  
  
ENV SLACK_ICON_URL=http://www.cloudpassage.com/wp-content/uploads/2016/12/don-
operator.png  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
# These arguments allow integration testing with the Halo API  
ARG HALO_API_KEY  
ARG HALO_API_SECRET_KEY  
ARG RUN_INTEGRATION_TESTS  
  
# Up to root to add additional packages  
USER root  
  
RUN apt-get install -y expect  
  
RUN pip install \  
pytest==3.1.1 \  
python-dotenv==0.8.2 \  
codeclimate-test-reporter==0.2.0 \  
pytest-cover==3.0.0  
  
# Drop in the app code  
COPY app/ /app/  
  
# Setup for manual library installation  
RUN mkdir /src/  
WORKDIR /src/  
  
COPY \--from=downloader /app/halocelery.tar.gz
/src/halocelery/halocelery.tar.gz  
  
RUN cd halocelery && \  
tar -zxvf ./halocelery.tar.gz && \  
cd /src/ && \  
mv ./halocelery /app  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
# Now take ownership and drop to non-root user  
RUN chown -R ${APP_USER}:$APP_GROUP /app  
  
USER ${APP_USER}  
  
RUN echo $RUN_INTEGRATION_TESTS  
  
# If RUN_INTEGRATION_TESTS is set, run integration tests.  
RUN if [ "$RUN_INTEGRATION_TESTS" = "True" ] ; \  
then echo "Run all tests" && \  
py.test --cov-report term-missing --cov=donlib --cov=cortexlib /app/test/ ; \  
else echo Not running integration tests!. && \  
py.test /app/test/unit ; \  
fi  
  
#####################################  
# Building the final container image  
FROM docker.io/halotools/python-sdk:ubuntu-16.04_sdk-1.1.4  
MAINTAINER toolbox@cloudpassage.com  
  
ENV SLACK_ICON_URL=http://www.cloudpassage.com/wp-content/uploads/2016/12/don-
operator.png  
ENV HALO_API_HOSTNAME=api.cloudpassage.com  
ENV HALO_API_PORT=443  
# Up to root to add additional packages  
USER root  
  
RUN apt-get install -y expect  
  
# Drop in the app code  
COPY app/ /app/  
  
# Setup for manual library installation  
RUN mkdir /src/  
WORKDIR /src/  
  
COPY \--from=downloader /app/halocelery.tar.gz
/src/halocelery/halocelery.tar.gz  
  
RUN cd halocelery && \  
tar -zxvf ./halocelery.tar.gz && \  
cd /src/ && \  
mv ./halocelery /app  
  
WORKDIR /app  
  
RUN pip install -r requirements.txt  
  
# Now take ownership and drop to non-root user  
RUN chown -R ${APP_USER}:$APP_GROUP /app  
  
USER ${APP_USER}  
  
WORKDIR /app  
  
CMD ["unbuffer", "python", "/app/runner.py"]  

