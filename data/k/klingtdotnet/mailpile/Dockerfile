FROM debian:latest  
MAINTAINER Andreas Linz <klingt.net@gmail.com>  
  
ENV DEBIAN_FRONTEND='noninteractive'  
RUN apt-get update  
RUN apt-get install -y \  
locales \  
curl \  
tar \  
python \  
python-pip \  
python-dev \  
libxml2-dev \  
libxslt1-dev \  
libz-dev &&\  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen &&\  
dpkg-reconfigure locales -f noninteractive &&\  
update-locale LANG='en_US.UTF-8'  
  
RUN MAILPILE_VERSION='0.5.2' &&\  
DEST='/opt/mailpile' && mkdir -p ${DEST} &&\  
curl -Ls
"https://github.com/mailpile/Mailpile/archive/${MAILPILE_VERSION}.tar.gz" |
tar --strip-components=1 -C "${DEST}" -xvzf - &&\  
pip install -r "${DEST}"/requirements.txt &&\  
ln -s "${DEST}"/mp /usr/local/bin/mp  
  
ENV MP_USER mpuser  
RUN useradd --create-home --system --shell $(which nologin) --comment
'Mailpile user' ${MP_USER}  
  
ENV LANG 'en_US.UTF-8'  
USER ${MP_USER}  
  
# initialize gpg home and mailpile by running a non mutable command  
RUN gpg --list-keys &&\  
mp quit  
  
EXPOSE 10080  
VOLUME /home/mpuser/.local/share/Mailpile  
VOLUME /home/mpuser/.gnupg  
  
CMD mp --www=0.0.0.0:10080 --wait  

