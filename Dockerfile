FROM node:14-alpine

# Install dependencies
RUN apk add --no-cache git python3 make g++ && \
    npm install -g svg-term-cli && \
    apk del git python3 make g++

# Set the working directory
WORKDIR /usr/src/app

# Entrypoint to pass arguments
ENTRYPOINT ["svg-term"]
