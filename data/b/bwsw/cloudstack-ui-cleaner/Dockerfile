FROM ubuntu:16.04  
MAINTAINER Bitworks Software info@bitworks.software  
  
ENV PAUSE 60  
ENV CS_API_ENDPOINT http://127.0.0.1:8080/client/api  
ENV CS_API_KEY
kW57SlDvz2NT3P9iQR94Vurpf_1lfOgmNQ1fR_CaPpDCn0N_7yHxCIVjSVnL4irnNYHSWRI41QUonU-
kRhny6A  
ENV CS_API_SECRET RRfrvAhJKabcHodonjdy5dT-
BETONdWzVxqEuRa0NJj67DodD4NXSccGyg5UOki3B-NkTs-gZGMl7ORsA_J7zA  
ENV DEBUG true  
ENV VOLUME_REMOVE_DELAY_MINUTES 10  
ENV TAG_KEY status  
ENV TAG_VALUE removed  
  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-dateutil git  
  
RUN git clone https://github.com/bwsw/cloudstack-python-client.git  
RUN cd cloudstack-python-client && python setup.py install  
  
COPY ./src /opt  
  
WORKDIR /opt  
  
CMD ["/bin/bash", "/opt/update-clean-objects"]

