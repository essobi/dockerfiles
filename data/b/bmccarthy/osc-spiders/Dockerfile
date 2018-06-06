#  
# Dockerfile for scrapyd  
#  
FROM vimagick/scrapyd  
  
LABEL maintainer="brian.mcc@rthy.org"  
  
COPY ./scrapyd.conf /etc/scrapyd/  
  
RUN mkdir -p /spiders  
COPY ./requirements.txt /spiders  
WORKDIR /spiders  
# RUN pip install -r requirements.txt  
RUN set -xe \  
&& pip install git+https://github.com/bmccarthy/extruct@handle-invalid-json \  
git+https://github.com/dateutil/dateutil.git \  
git+https://github.com/kennethreitz/requests.git  
  
# stresfactory - WARNING: Remote certificate is not valid for hostname
"stressfactory.com"; VerificationError(errors=[DNSMismatch  
# (mismatched_id=DNS_ID(hostname='stressfactory.com'))])  
# when running docker run -i -t <image_name> bash - need to pass osc_api  
COPY . /spiders  
  
WORKDIR /spiders/osc  
  
CMD ["start_docker.sh"]

