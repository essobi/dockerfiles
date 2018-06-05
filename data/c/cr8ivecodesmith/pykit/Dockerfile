FROM python:latest  
MAINTAINER matt lebrun <matt@lebrun.org>  
  
# Configure locales  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
# Install Tini  
# https://github.com/krallin/tini  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.9.0/tini >
tini && \  
echo "faafbfb5b079303691a939a747d7f60591f2143164093727e870b289a44d9872 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
ADD requirements.txt /  
RUN pip install -r requirements.txt  
  
RUN apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& apt-get purge -y \  
&& rm -r /requirements.txt  
  
ENTRYPOINT ["tini", "--"]  
CMD ["ipython"]  

