FROM python:2.7  
MAINTAINER Beshr Kayali "me@beshr.com"  
# Setup  
ENV BASE=/base  
ENV REQS=reqs.txt  
  
# Install Tini  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Add a notebook profile.  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
# Update and stuff  
RUN apt-get update  
RUN apt-get install -y \  
time \  
sudo \  
bash  
  
# Install requirements  
RUN echo "Upgrade setuptools and pip" \  
&& pip install -U setuptools pip  
  
COPY requirements.txt $BASE/$REQS  
RUN echo "Installing requirements..."  
RUN time pip install --no-cache-dir -r $BASE/$REQS  
  
# Install spacy English data  
RUN python -m spacy.en.download all  
  
WORKDIR /src  
EXPOSE 8888  
ENTRYPOINT ["tini", "--"]  
CMD ["jupyter", "notebook"]  

