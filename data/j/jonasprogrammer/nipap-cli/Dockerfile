FROM python:3-stretch  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends bash-completion \  
&& pip --no-input install envtpl \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo '#!/bin/sh' >/usr/bin/rst2man \  
&& echo 'touch $2' >>/usr/bin/rst2man \  
&& chmod +x /usr/bin/rst2man  
  
COPY nipap/nipap-cli /nipap  
COPY nipap/pynipap /nipap/pynipap  
COPY nipaprc-cli /nipap/nipaprc  
WORKDIR /nipap  
RUN cd /nipap/pynipap && python setup.py install && cd /nipap \  
&& pip --no-input install -r requirements.txt \  
&& python setup.py install  
  
ENV NIPAP_PORT 1337  
COPY entrypoint-cli.sh /nipap/entrypoint.sh  
ENTRYPOINT ["/nipap/entrypoint.sh"]  
CMD ["bash"]  

