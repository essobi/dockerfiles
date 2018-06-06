FROM ubuntu:14.04  
# Install necessary applications for feature extraction (libsvm, maxent, etc.)  
RUN sudo apt-get update && sudo apt-get install g++ git zlib1g-dev gfortran
python-dev doxygen python-setuptools wget git build-essential -y  
RUN rm -fR build_deps  
RUN mkdir -p build_deps  
WORKDIR /tmp/build_deps  
RUN GIT_SSL_NO_VERIFY=1 wget
http://pkgs.fedoraproject.org/repo/pkgs/libsvm/libsvm-2.91.tar.gz/aec07b9142ce585c95854ed379538154/libsvm-2.91.tar.gz  
RUN tar -zxf libsvm-2.91.tar.gz  
WORKDIR /tmp/build_deps/libsvm-2.91  
RUN make lib  
RUN sudo cp libsvm.so.1 /usr/local/lib  
RUN GIT_SSL_NO_VERIFY=1 git clone https://github.com/lzhang10/maxent.git  
WORKDIR /tmp/build_deps/libsvm-2.91/maxent  
RUN ./configure  
RUN make  
RUN sudo make install  
WORKDIR /tmp/build_deps/libsvm-2.91/maxent/python  
RUN python setup.py install  
RUN sudo ldconfig  
  
# install all necessary applications for genre classification  
RUN sudo apt-get update && sudo apt-get install -y \  
cmake \  
python2.7 \  
python3-matplotlib  
# install tinyest  
WORKDIR /tmp  
RUN rm * -Rf  
RUN git clone https://github.com/danieldk/tinyest.git /tmp  
WORKDIR /tmp  
RUN cmake .  
RUN make  
RUN sudo make install  
RUN rm -Rf /tmp/*  
  
# Setup SSH keys to download the necessary corpora and  
# source code for the feature extraction  
#ADD id_rsa.pub /root/test  
#RUN ls  
RUN mkdir -p /root/.ssh  
#RUN touch ~/.ssh/known_hosts  
#RUN ssh-keygen -R bitbucket.org  
RUN ssh-keyscan -t rsa bitbucket.org > ~/.ssh/known_hosts  
#RUN ./iter-genreclassification.py  
ADD id_rsa /root/.ssh/id_rsa  
RUN chmod 700 /root/.ssh/id_rsa  
ADD id_rsa.pub /root/.ssh/id_rsa.pub  
RUN chmod 700 /root/.ssh/id_rsa.pub  
  
# Install training and testing corpora for the four different genres
(educational, scientific prose, literature, journalism)  
# And install programs necessary for feature extraction  
##Uncomment the following line to break the cache and pull the new source from
git (if this has changed)  
#ADD
http://www.random.org/strings/?num=10&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new
uuid  
RUN mkdir /home/feature-extraction-tools  
RUN git clone git@bitbucket.org:acimino/genrenlptools.git /home/feature-
extraction-tools  
  
# download the grafting-genreclassification software  
RUN mkdir /home/grafting-genreclassification  
##Uncomment the following line to break the cache and pull the new source from
git (if this has changed)  
#ADD
http://www.random.org/strings/?num=10&len=8&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new
uuid  
RUN git clone https://github.com/wieling/grafting-genreclassification.git
/home/grafting-genreclassification  
WORKDIR /home/grafting-genreclassification  
RUN chmod +x *.py  
RUN mkdir results  
RUN mkdir tmp  
RUN mkdir input  
  
# Run feature extraction for 100 top words and 91 syntactic features  
WORKDIR /home/feature-extraction-tools  
RUN bash run.sh Confs/syntax+100tw.conf  
  
# Copy extracted features for each document set to input directory of grafting
application  
WORKDIR /home/grafting-genreclassification/input  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/FeatNames.txt .  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/testing.grafting .  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/Journalism.parsed.grafting
train_Journalism.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/Educational.parsed.grafting
train_Educational.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/Literature.parsed.grafting
train_Literature.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/syntax+100tw/ScientificProse.parsed.grafting
train_ScientificProse.parsed.grafting  
  
# Ignore length of the document as a feature, as it is an unfair feature given
that educational and journalism texts are much shorter than the other two
types  
RUN /bin/echo 'lunghezzaDOC' > excluded.txt  
  
WORKDIR /home/grafting-genreclassification  
RUN ./iter-genreclassification.py  
  
# Change foldernames  
RUN mv results results-syntax100tw  
RUN mv input input-syntax100tw  
RUN mv tmp tmp-syntax100tw  
RUN mkdir input  
RUN mkdir results  
RUN mkdir tmp  
  
# Run feature extraction for 200 top words  
WORKDIR /home/feature-extraction-tools  
RUN bash run.sh Confs/200tw.conf  
  
# Copy extracted features for each document set to input directory of grafting
application  
WORKDIR /home/grafting-genreclassification/input  
RUN cp /home/feature-extraction-tools/extracted_features/200tw/FeatNames.txt .  
RUN cp /home/feature-extraction-
tools/extracted_features/200tw/testing.grafting .  
RUN cp /home/feature-extraction-
tools/extracted_features/200tw/Journalism.parsed.grafting
train_Journalism.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/200tw/Educational.parsed.grafting
train_Educational.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/200tw/Literature.parsed.grafting
train_Literature.parsed.grafting  
RUN cp /home/feature-extraction-
tools/extracted_features/200tw/ScientificProse.parsed.grafting
train_ScientificProse.parsed.grafting  
  
# Ignore length of the document as a feature, as it is an unfair feature given
that educational and journalism texts are much shorter than the other two
types  
RUN /bin/echo 'lunghezzaDOC' > excluded.txt  
  
WORKDIR /home/grafting-genreclassification  
RUN ./iter-genreclassification.py  
  
# Change foldernames  
RUN mv results results-200tw  
RUN mv input input-200tw  
RUN mv tmp tmp-200tw  

