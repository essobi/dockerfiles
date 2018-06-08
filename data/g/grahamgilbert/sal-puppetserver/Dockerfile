FROM grahamgilbert/puppetserver:2.3.0  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
  
ENV SAL_PUPPETSERVER_URL='http://sal' SAL_PUPPETSERVER_PRIVATE_KEY=123 \  
SAL_PUPPETSERVER_PUBLIC_KEY=123 \  
SAL_PUPPETSERVER_VERIFY=True  
RUN apt-get install -y python-setuptools python-dev libffi-dev libssl-dev \  
&& easy_install pip && pip install requests pyOpenSSL ndg-httpsclient pyasn1  
ADD sal_cert.py /sal_cert.py  
RUN chmod 755 /sal_cert.py  
RUN touch /var/log/check_csr.out  
RUN chown puppet:puppet /var/log/check_csr.out  

