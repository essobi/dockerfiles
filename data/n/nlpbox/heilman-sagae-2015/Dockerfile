# Dockerfile to build, run and train the Heilman and Sagae (2015)  
# RST discourse parser on the RST Discourse Treebank (RST-DT)  
FROM nlpbox/nlpbox-base:16.04  
# General Setup  
# =============  
# we need lots of libraries for building numpy/scipy  
RUN apt-get update -y && apt-get install -y build-essential python-dev \  
python-pip python3-dev python3-pip \  
libblas-dev liblapack-dev libamd2.4.1 libblas3 libc6 \  
libgcc1 libgfortran3 liblapack3 libumfpack5.7.1 libstdc++6 gfortran \  
python-all-dev libatlas-base-dev && \  
pip3 install python-zpar  
  
# Prerequisite: ZPAR models for English  
# -------------------------------------  
WORKDIR /opt/zpar-0.7/models  
RUN wget -O english.zip
http://sourceforge.net/projects/zpar/files/0.7/english.zip/download  
RUN dtrx english.zip  
RUN rm english.zip  
  
# Prerequisite: CRF++  
# -------------------  
WORKDIR /opt  
# the original version of CRF++ https://github.com/taku910/crfpp.git does not  
# compile, because winmain.h is missing, so we'll use this patched version  
# instead  
RUN git clone -b patch https://github.com/hiroshi-umemoto/crfpp  
  
WORKDIR /opt/crfpp  
RUN ./configure && make && make install && ldconfig  
  
# Installing Heilman and Sagae (2015)  
# -----------------------------------  
WORKDIR /opt  
RUN git clone -b feature/update_skll https://github.com/arne-cl/discourse-
parsing.git && echo  
WORKDIR /opt/discourse-parsing  
  
RUN pip3 install -r requirements.txt && \  
python3.5 setup.py install # make entry points scripts accessible  
  
RUN python3.5 -c "import nltk; nltk.download('punkt')"  
RUN python3.5 -c "import nltk; nltk.download('maxent_treebank_pos_tagger')"  
RUN python3 -c "import nltk; nltk.download('averaged_perceptron_tagger')"  
  
ENV ZPAR_LIBRARY_DIR /usr/local/lib/python3.5/dist-packages/zpar/dist  
ENV ZPAR_MODEL_DIR /opt/zpar-0.7/models/english  
  
  
# add script for training the parser on the RST-DT corpus  
ADD train_discourse_parser.sh /opt/discourse-parsing/  
  
# add models trained on RST-DT, the training log and test files  
ADD segmentation_model.C32.0 train_discourse_parser.log article.txt
input_*.txt test_hs2015.py hs2015.sh /opt/discourse-parsing/  
ADD rst_parsing_model.C0.5 /opt/discourse-parsing/rst_parsing_model.C0.5  
  
RUN pip3 install sh # needed for unit tests  
  
# by default the container runs the rst_parse command with the supplied model
on article.txt  
# cf. https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd/  
ENTRYPOINT ["/usr/local/bin/rst_parse", "--segmentation_model",
"segmentation_model.C32.0", "--parsing_model", "rst_parsing_model.C0.5"]  
CMD ["/opt/discourse-parsing/article.txt"]  

