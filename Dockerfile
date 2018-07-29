FROM ubuntu:bionic
ENV NODEJS_VERSION=8.11.2 \
    PATH=$PATH:/opt/node/bin

WORKDIR "/opt/node"

# Install Node
RUN apt-get -qq update && apt-get -qq install -y curl ca-certificates --no-install-recommends && \
    curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install dependency for yarn
RUN apt-get update && apt-get install -y wget gnupg

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn

RUN apt-get update && \
    apt-get install -y \
        python3-pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD package.json /code/
ADD yarn.lock /code/
RUN yarn install
RUN yarn global add browserify yuglify sass

ADD . /code/
