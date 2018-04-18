FROM ubuntu:16.04
MAINTAINER yskn67

WORKDIR /tmp/
RUN apt-get update -y && apt-get install -yq wget unzip build-essential gcc zlib1g-dev python3 python3-dev python3-pip
RUN wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/
RUN apt-get install libappindicator1 -yq
RUN touch /etc/default/google-chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; exit 0
RUN apt-get install -fyq
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN pip3 install selenium

WORKDIR /
