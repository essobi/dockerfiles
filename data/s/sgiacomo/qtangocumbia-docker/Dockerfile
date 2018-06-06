FROM debian:stretch  
  
# Update the repo info  
RUN apt-get update  
  
# change installation dialogs policy to noninteractive  
# otherwise debconf raises errors: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# install and configure supervisor  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
RUN apt-get install -y procps  
  
RUN apt-get install -y default-mysql-server  
  
RUN apt-get install -y tango-db liblog4tango-dev libtango-dev  
  
RUN apt-get install -y tango-test  
  
RUN apt-get install -y git vim xvfb  
  
#  
# Qt, designer, qtcreator, Qwt libraries for plots  
#  
RUN apt-get install -y qt5-default libqwt-qt5-6 libqwt-qt5-dev
libqt5x11extras5 libqt5x11extras5-dev libqt5designercomponents5 qttools5-dev
qttools5-dev-tools libxmu-dev qtcreator  
  
# Java  
#  
RUN apt-get install -y net-tools openjdk-8-jre-headless openjdk-8-jdk  
  
# Tools to generate documentation  
RUN apt-get install -y git doxygen graphviz  
  
# Autotools, build tools  
RUN apt-get install -y build-essential autoconf libtool  
  
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig  
  
WORKDIR /var/lib  
  
RUN git clone https://github.com/ELETTRA-SincrotroneTrieste/cppqtclients.git  
  
WORKDIR /var/lib/cppqtclients/cumbia  
  
# REMOVE THIS  
RUN git pull && echo OK && echo OK && echo OK  
  
RUN autoconf && libtoolize && automake --add-missing  
RUN ./configure --prefix=/usr/local \--includedir=/usr/local/include/cumbia  
RUN make -j4 && make install  
  
# REMOVE THIS  
RUN git pull && echo OK  
  
WORKDIR /var/lib/cppqtclients/cumbia-tango  
RUN autoconf && libtoolize && automake --add-missing  
RUN ./configure --prefix=/usr/local \--includedir=/usr/local/include/cumbia-
tango  
RUN make -j4 && make install  
  
WORKDIR /var/lib/cppqtclients/cumbia-qtcontrols  
  
# REMOVE THIS  
RUN git pull && echo OK  
  
RUN qmake && make -j5 && make install  
  
#remove this  
RUN git pull && echo OK && echo OK && echo OK && echo OK  
  
WORKDIR /var/lib/cppqtclients/qumbia-tango-controls  
RUN qmake && make -j5 && make install  
  
WORKDIR /var/lib/cppqtclients/qumbia-tango-controls/plugins  
RUN qmake && make -j5 && make install  
  
WORKDIR /var/lib/cppqtclients/qtango  
  
# remove this!  
RUN git pull && echo oK && echo OK  
  
RUN qmake && make -j5 && make install  
  
# configure supervisord  
COPY supervisord.conf /etc/supervisor/conf.d/  
  
# Jive  
RUN mkdir /var/lib/tango-java/  
COPY Jive-7.16-jar-with-dependencies.jar /var/lib/tango-java/  
COPY jive.sh /usr/local/bin  
  
# copy & untar mysql tango database and change owner to mysql user  
ADD tangodb-tiny.tar /var/lib/mysql/  
RUN mkdir -p /var/run/mysqld  
RUN chown -R mysql /var/run/mysqld  
RUN chown -R mysql /var/lib/mysql/tango  
  
# define tango host env var  
ENV TANGO_HOST qtangocumbia:10000  
ENV QT_PLUGIN_PATH /usr/local/lib/qumbia-tango-
controls/plugins:/usr/local/lib/plugins  
  
# configure virtual monitor env variable  
ENV DISPLAY :0.0  
RUN useradd -ms /bin/bash dancer  
  
# /usr/local/lib in ld path  
COPY cumbialibs.conf /etc/ld.so.conf.d  
  
RUN ldconfig  
  
CMD ["/usr/bin/supervisord"]  
  

